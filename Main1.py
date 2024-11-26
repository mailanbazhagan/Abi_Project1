import streamlit as st
import random

# Expanded word collections with clues
WORD_COLLECTIONS = {
    'Science': {
        'Easy': [
            {'word': 'atom', 'clue': 'Smallest unit of matter'},
            {'word': 'cell', 'clue': 'Basic building block of life'},
            {'word': 'gene', 'clue': 'Hereditary unit in DNA'},
            {'word': 'moon', 'clue': 'Earth\'s natural satellite'},
            {'word': 'star', 'clue': 'Luminous sphere of plasma'},
            {'word': 'plant', 'clue': 'Living organism that produces its own food'},
            {'word': 'water', 'clue': 'Transparent liquid essential for life'},
            {'word': 'virus', 'clue': 'Microscopic infectious agent'},
            {'word': 'brain', 'clue': 'Organ of soft nervous tissue'},
            {'word': 'earth', 'clue': 'Third planet from the sun'}
        ],
        'Medium': [
            {'word': 'plasma', 'clue': 'Fourth state of matter'},
            {'word': 'genome', 'clue': 'Complete set of genetic material'},
            {'word': 'neuron', 'clue': 'Nerve cell that transmits signals'},
            {'word': 'photon', 'clue': 'Quantum of electromagnetic radiation'},
            {'word': 'magnet', 'clue': 'Object that produces magnetic field'},
            {'word': 'quantum', 'clue': 'Discrete quantity of energy'},
            {'word': 'protein', 'clue': 'Essential molecule for cell function'},
            {'word': 'enzyme', 'clue': 'Biological catalyst'},
            {'word': 'molecule', 'clue': 'Group of atoms bonded together'},
            {'word': 'gravity', 'clue': 'Force of attraction between masses'}
        ],
        'Hard': [
            {'word': 'mitochondria', 'clue': 'Cellular powerhouse producing energy'},
            {'word': 'chromosome', 'clue': 'DNA-containing structure in cells'},
            {'word': 'thermodynamics', 'clue': 'Study of heat and energy transfer'},
            {'word': 'radioactivity', 'clue': 'Emission of radiation from unstable nuclei'},
            {'word': 'photosynthesis', 'clue': 'Process by which plants make food'},
            {'word': 'astrophysics', 'clue': 'Branch studying celestial objects'},
            {'word': 'electromagnetic', 'clue': 'Relating to electricity and magnetism'},
            {'word': 'biotechnology', 'clue': 'Technology using biological systems'},
            {'word': 'nanotechnology', 'clue': 'Manipulation of matter on atomic scale'},
            {'word': 'bioinformatics', 'clue': 'Applying computer science to biology'}
        ]
    },
    'Technology': {
        'Easy': [
            {'word': 'code', 'clue': 'Instructions for computer programs'},
            {'word': 'web', 'clue': 'Global information system'},
            {'word': 'app', 'clue': 'Software application'},
            {'word': 'data', 'clue': 'Information processed by computer'},
            {'word': 'net', 'clue': 'Short for internet'},
            {'word': 'disk', 'clue': 'Storage device for digital data'},
            {'word': 'link', 'clue': 'Connection between web pages'},
            {'word': 'site', 'clue': 'Location on the World Wide Web'},
            {'word': 'chip', 'clue': 'Integrated electronic circuit'},
            {'word': 'file', 'clue': 'Collection of data or program'}
        ],
        'Medium': [
            {'word': 'server', 'clue': 'Computer that provides data to other computers'},
            {'word': 'python', 'clue': 'Popular programming language'},
            {'word': 'cloud', 'clue': 'Remote storage and computing service'},
            {'word': 'cyber', 'clue': 'Related to computer networks'},
            {'word': 'robot', 'clue': 'Automated machine'},
            {'word': 'network', 'clue': 'Interconnected computing devices'},
            {'word': 'mobile', 'clue': 'Portable communication device'},
            {'word': 'coding', 'clue': 'Process of writing computer programs'},
            {'word': 'system', 'clue': 'Set of connected things working together'},
            {'word': 'digital', 'clue': 'Using or representing data as numbers'}
        ],
        'Hard': [
            {'word': 'algorithm', 'clue': 'Step-by-step procedure for calculations'},
            {'word': 'blockchain', 'clue': 'Decentralized and distributed digital ledger'},
            {'word': 'cybersecurity', 'clue': 'Protection of computer systems'},
            {'word': 'cryptocurrency', 'clue': 'Digital or virtual currency'},
            {'word': 'neuralnetwork', 'clue': 'Computing system inspired by brain'},
            {'word': 'quantumcomputing', 'clue': 'Computing using quantum-mechanical phenomena'},
            {'word': 'artificialintelligence', 'clue': 'Machine intelligence mimicking human cognition'},
            {'word': 'machinlearning', 'clue': 'AI system that improves from experience'},
            {'word': 'deeplearning', 'clue': 'Machine learning using neural networks'},
            {'word': 'virtualization', 'clue': 'Creating virtual version of computing resources'}
        ]
    }
}

# Scientist names based on performance
SCIENTIST_RATINGS = [
    ('Novice Learner', (0, 20)),
    ('Emerging Researcher', (21, 40)),
    ('Junior Scientist', (41, 60)),
    ('Research Associate', (61, 80)),
    ('Distinguished Scientist', (81, 100)),
    ('Nobel Laureate', (101, float('inf')))
]

class WordGuessingGame:
    def __init__(self, domain, complexity):
        self.words = WORD_COLLECTIONS[domain][complexity]
        random.shuffle(self.words)
        self.total_score = 0
        self.current_word_index = 0
        self.attempts = {}  # Track attempts for each word

    def generate_masked_word(self, word):
        # Mask 30-50% of characters
        mask_count = max(1, len(word) // 2)
        masked_indices = random.sample(range(len(word)), mask_count)
        masked_word = list(word)
        for idx in masked_indices:
            masked_word[idx] = '_'
        return ''.join(masked_word), masked_indices

    def check_guess(self, guess, word, masked_indices):
        if len(guess) != len(word):
            return False
        
        guess_list = list(guess)
        for idx in masked_indices:
            if guess_list[idx] != word[idx]:
                return False
        return True

    def get_scientist_title(self, score):
        for title, (min_score, max_score) in SCIENTIST_RATINGS:
            if min_score <= score <= max_score:
                return title
        return 'Novice Learner'

def main():
    st.title('Word Guessing Challenge')
    
    # Sidebar for game configuration
    st.sidebar.header('Game Setup')
    domain = st.sidebar.selectbox('Choose Domain', 
                                  list(WORD_COLLECTIONS.keys()))
    complexity = st.sidebar.selectbox('Choose Complexity', 
                                      ['Easy', 'Medium', 'Hard'])
    
    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = WordGuessingGame(domain, complexity)
    
    game = st.session_state.game
    
    # If all words have been guessed
    if game.current_word_index >= 10:
        st.success(f"Game Over! 🎉")
        total_score = game.total_score
        scientist_title = game.get_scientist_title(total_score)
        st.balloons()
        st.write(f"🏆 Your Score: {total_score}")
        st.write(f"🔬 You are now a {scientist_title}!")
        
        if st.button('Play Again'):
            st.session_state.game = WordGuessingGame(domain, complexity)
            game = st.session_state.game
            st.rerun()  # Changed from experimental_rerun()
    
    if game.current_word_index < 10:
        current_word_dict = game.words[game.current_word_index]
        current_word = current_word_dict['word']
        
        # Initialize attempts for this word if not already set
        if current_word not in game.attempts:
            game.attempts[current_word] = 0
        
        masked_word, masked_indices = game.generate_masked_word(current_word)
        
        st.header(f"Word {game.current_word_index + 1}")
        
        # Display clue
        st.info(f"🔍 Clue: {current_word_dict['clue']}")
        
        st.subheader(f"Guess the Word: {masked_word}")
        
        # Attempts tracking
        if game.attempts[current_word] < 2:
            guess = st.text_input("Your Guess", max_chars=len(current_word))
            
            if st.button('Submit Guess'):
                game.attempts[current_word] += 1
                
                if game.check_guess(guess, current_word, masked_indices):
                    # First attempt
                    if game.attempts[current_word] == 1:
                        game.total_score += 5
                        st.success("Correct! 🎊 (+5 points)")
                    # Second attempt
                    else:
                        game.total_score += 2
                        st.success("Correct! 🎊 (+2 points)")
                    
                    game.current_word_index += 1
                    st.rerun()  # Changed from experimental_rerun()
                else:
                    # First incorrect attempt
                    if game.attempts[current_word] == 1:
                        st.warning("Incorrect guess. Try again!")
                    # Second incorrect attempt
                    else:
                        st.error(f"Wrong guess! Correct word was: {current_word}")
                        game.current_word_index += 1
                        st.rerun()  # Changed from experimental_rerun()
        else:
            # If both attempts are used
            st.error(f"No more attempts! Correct word was: {current_word}")
            game.current_word_index += 1
            st.rerun()  # Changed from experimental_rerun()

if __name__ == '__main__':
    main()