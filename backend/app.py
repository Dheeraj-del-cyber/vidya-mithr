from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

knowledge_base = {

    
    "ohms law": "Ohm’s Law states that V = IR, where V is voltage, I is current, and R is resistance.",
    "newtons first law": "Newton’s First Law states that a body remains at rest or in uniform motion unless acted upon by an external force.",
    "newtons second law": "Newton’s Second Law states that Force equals Mass multiplied by Acceleration (F = ma).",
    "newtons third law": "Newton’s Third Law states that for every action, there is an equal and opposite reaction.",
    "kirchhoff current law": "Kirchhoff’s Current Law states that the algebraic sum of currents at a node is zero.",
    "kirchhoff voltage law": "Kirchhoff’s Voltage Law states that the algebraic sum of voltages in a closed loop is zero.",
    "coulombs law": "Coulomb’s Law describes the force between two charged particles.",
    "faradays law": "Faraday’s Law states that a change in magnetic flux induces an electromotive force.",

    "integration": "Integration is the process of finding the area under a curve and is the inverse of differentiation.",
    "definite integral": "A definite integral calculates the exact area under a curve between two limits.",
    "indefinite integral": "An indefinite integral represents a family of functions and includes a constant of integration.",
    "derivative": "A derivative represents the rate of change of a function with respect to a variable.",
    "limit": "A limit describes the behavior of a function as the input approaches a particular value.",
    "matrix": "A matrix is a rectangular array of numbers arranged in rows and columns.",
    "determinant": "The determinant is a scalar value that provides important properties of a square matrix.",
    "eigenvalue": "An eigenvalue is a scalar that describes how a linear transformation affects a vector.",
    "probability": "Probability measures the likelihood of an event occurring, ranging from 0 to 1.",
    "1+1":"2",
    "2+2":"4",
    "10+10":"20",
    "1500+1500":"3000",

    

   
    "algorithm": "An algorithm is a finite, step-by-step procedure used to solve a problem.",
    "time complexity": "Time complexity measures the amount of time an algorithm takes as a function of input size.",
    "space complexity": "Space complexity measures the amount of memory an algorithm uses.",
    "data structure": "A data structure is a way of organizing data for efficient access and modification.",
    "stack": "A stack is a linear data structure that follows the Last In First Out (LIFO) principle.",
    "queue": "A queue is a linear data structure that follows the First In First Out (FIFO) principle.",
    "linked list": "A linked list is a dynamic data structure where elements are connected using pointers.",
    "binary tree": "A binary tree is a hierarchical data structure where each node has at most two children.",
    "database": "A database is an organized collection of structured data stored electronically.",
    "sql": "SQL is a language used to manage and manipulate relational databases.",
    "operating system": "An operating system manages computer hardware and software resources.",
    "deadlock": "Deadlock is a condition where processes are unable to proceed because each is waiting for resources held by others.",
    "computer network": "A computer network is a group of interconnected devices that communicate with each other.",

    
    "ai": "Artificial Intelligence refers to machines that simulate human intelligence processes.",
    "machine learning": "Machine learning is a subset of AI that enables systems to learn from data.",
    "deep learning": "Deep learning is a type of machine learning that uses neural networks with multiple layers.",
    "supervised learning": "Supervised learning uses labeled data to train machine learning models.",
    "unsupervised learning": "Unsupervised learning finds patterns in data without labeled outputs.",
    "neural network": "A neural network is a computational model inspired by the human brain.",

    "academic companion": "An academic companion is a digital assistant that helps students with learning and doubt resolution.",
    "personalized learning": "Personalized learning adapts content to the learner’s pace and understanding.",
    "learning gap": "A learning gap occurs when a student misses foundational concepts required for future learning.",
    "when is sslc final exam":"currently the official date is not announced",

    
    "what is vidya mitra": "Vidya Mitra is an academic companion designed to provide accurate, instant doubt resolution using verified academic content.",
    "how does vidya mitra work": "The system retrieves answers from a curated knowledge base based on user queries.",
    "how is accuracy ensured": "Accuracy is ensured by using syllabus-aligned, pre-verified academic content rather than open-ended AI generation.",
    "is this real ai": "This is a rule-based prototype demonstrating the concept; AI integration is planned in the full version.",
    "why not use live ai": "Live AI can generate incorrect or hallucinated answers; our approach prioritizes correctness and trust.",
    "what problem does it solve": "It addresses unresolved academic doubts caused by limited access to personalized guidance.",
    "target users": "The target users are students who require instant academic support outside classroom hours.",
    "future scope": "Future scope includes AI-powered retrieval, teacher-reviewed content, and expansion to more subjects.",
    "scalability": "The system is scalable by expanding the knowledge base and integrating AI-based retrieval models.",

    "units and dimensions": "Units and dimensions are used to measure physical quantities and check the correctness of equations.",
    "scalar quantity": "A scalar quantity has only magnitude and no direction.",
    "vector quantity": "A vector quantity has both magnitude and direction.",
    "uniform motion": "Uniform motion is motion with constant velocity.",
    "acceleration": "Acceleration is the rate of change of velocity with time.",
    "laws of motion": "Newton’s laws of motion describe the relationship between force, mass, and motion.",
    "work energy theorem": "The work-energy theorem states that work done equals change in kinetic energy.",
    "law of conservation of energy": "Energy can neither be created nor destroyed, only transformed.",
    "center of mass": "The center of mass is the point where the entire mass of a system is considered to be concentrated.",
    "pressure": "Pressure is force applied per unit area.",
    "buoyancy": "Buoyancy is the upward force exerted by a fluid on an object immersed in it.",
    "bernoulli principle": "Bernoulli’s principle states that an increase in fluid speed results in a decrease in pressure.",

    
    "electric field": "An electric field is the region around a charge where it experiences force.",
    "electric potential": "Electric potential is the work done per unit charge.",
    "capacitance": "Capacitance is the ability of a system to store electric charge.",
    "alternating current": "Alternating current periodically reverses direction.",
    "electromagnetic induction": "Electromagnetic induction is the generation of emf due to changing magnetic flux.",
    "lcr circuit": "An LCR circuit consists of an inductor, capacitor, and resistor.",
    "electromagnetic waves": "Electromagnetic waves are transverse waves consisting of electric and magnetic fields.",
    "photoelectric effect": "The photoelectric effect is the emission of electrons when light strikes a metal surface.",
    "atomic model": "An atomic model explains the structure and behavior of atoms.",
    "semiconductor": "A semiconductor has conductivity between a conductor and an insulator.",
    "pn junction": "A PN junction is formed by joining p-type and n-type semiconductors.",

  
    "atomic structure": "Atomic structure describes the arrangement of electrons, protons, and neutrons.",
    "quantum numbers": "Quantum numbers describe the position and energy of electrons in atoms.",
    "periodic table": "The periodic table arranges elements based on atomic number and properties.",
    "chemical bonding": "Chemical bonding is the force that holds atoms together in molecules.",
    "ionic bond": "An ionic bond is formed by transfer of electrons.",
    "covalent bond": "A covalent bond is formed by sharing of electrons.",
    "states of matter": "Matter exists as solid, liquid, or gas depending on energy and arrangement of particles.",
    "thermodynamics": "Thermodynamics deals with energy changes in chemical reactions.",
    "enthalpy": "Enthalpy represents the heat content of a system.",
    "equilibrium": "Chemical equilibrium is a state where forward and reverse reactions occur at equal rates.",

    
    "electrochemistry": "Electrochemistry studies chemical reactions involving electricity.",
    "electrochemical cell": "An electrochemical cell converts chemical energy into electrical energy.",
    "chemical kinetics": "Chemical kinetics studies the rate of chemical reactions.",
    "rate of reaction": "Rate of reaction is the change in concentration per unit time.",
    "surface chemistry": "Surface chemistry deals with phenomena at interfaces.",
    "coordination compounds": "Coordination compounds contain a central metal atom bonded to ligands.",
    "haloalkanes": "Haloalkanes are organic compounds containing halogen atoms.",
    "alcohols": "Alcohols are organic compounds containing the hydroxyl group.",
    "biomolecules": "Biomolecules include carbohydrates, proteins, lipids, and nucleic acids.",
    "polymers": "Polymers are large molecules made from repeating units.",
    "chemistry in everyday life": "Chemistry in everyday life includes drugs, detergents, and food additives.",

  
    "sets": "A set is a collection of well-defined objects.",
    "relations and functions": "Relations and functions describe connections between sets.",
    "trigonometry": "Trigonometry deals with angles and sides of triangles.",
    "complex numbers": "Complex numbers consist of a real and an imaginary part.",
    "quadratic equations": "Quadratic equations are equations of degree two.",
    "permutations": "Permutations deal with arrangements of objects.",
    "combinations": "Combinations deal with selections of objects.",
    "binomial theorem": "The binomial theorem expands expressions raised to powers.",
    "coordinate geometry": "Coordinate geometry studies geometry using algebra.",
    "statistics": "Statistics involves collection and analysis of data.",

   
    "mathematical induction": "Mathematical induction is a method to prove statements for natural numbers.",
    "inverse trigonometric functions": "Inverse trigonometric functions reverse trigonometric operations.",
    "continuity": "Continuity means a function has no breaks.",
    "differentiability": "Differentiability means a function has a defined derivative.",
    "applications of derivatives": "Derivatives are used to find maxima, minima, and rates of change.",
    "integrals": "Integrals are used to find areas and solve differential equations.",
    "differential equations": "Differential equations involve derivatives of functions.",
    "vectors": "Vectors represent quantities with magnitude and direction.",
    "three dimensional geometry": "3D geometry studies points, lines, and planes in space.",
    "linear programming": "Linear programming optimizes a linear objective function.",
    "probability distribution": "Probability distribution describes the likelihood of outcomes.",

   
    "why is this reliable": "The system uses syllabus-aligned, pre-verified academic knowledge.",
    "how is this different from chatgpt": "Unlike generative AI, this system avoids hallucinations by using fixed academic content.",
    "is it scalable": "Yes, the system scales by expanding the curated knowledge base or adding AI retrieval later.",
    "real world impact": "It helps students clear doubts instantly and reduces learning gaps."
}
@app.route("/ask", methods=["POST"])
def ask():
    question = request.get_json().get("question", "").lower()

    for key in knowledge_base:
        if key in question:
            return jsonify({"answer": knowledge_base[key]})

    return jsonify({
        "answer": "This question will be answered using verified academic sources in the full version.THANK YOU"
    })

if __name__ == "__main__":
    app.run(debug=True)