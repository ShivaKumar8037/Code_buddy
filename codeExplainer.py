import streamlit as st
from palm_api import palmAPI
import streamlit.components.v1 as components



def codeExplainer(exampleCode, api_key):
    st.write("Explanation: ")
    explanation = palmAPI(api_key, f"Explain this code in simple terms : {exampleCode}")
    return explanation






mermaid_rules = """
Flowcharts: 'flowchart [TB|BT|RL|LR]': Top-Bottom, Bottom-Top, Right-Left, Left-Right. 
Nodes: 'id[Text]', 'id(Text)', 'id>{Text}', 'id{{Text}}', '-->', '---', '==>', '-.->'. 
Subgraphs: 'subgraph id[Title] ... end'. 
Links: 'A -->|text| B', 'click nodeId callback()'.

Sequence Diagrams: 'sequenceDiagram'. 
Participants: 'participant', 'actor'. 
Messages: '-->', '-->>', '-x', '-\\>', 'Note right of', 'Note left of', 'Note over'. 
Loops: 'loop', 'end'. 
Alt, Opt: 'alt', 'else', 'opt', 'end'.

Class Diagrams: 'classDiagram'. 
Class: 'class ClassName'. 
Methods, Properties: '--', '++', '...', '<<', '>>'. 
Relationships: '--', '<|--', '-->', '<|..', '..|>', 'o--', 'o..', '..o', '--o'.

State Diagrams: 'stateDiagram-v2'. 
States: 'state StateName'. 
Transitions: '-->', '[*] -->'. 
Nested States: 'state StateName { ... }'.

Gantt Charts: 'gantt'. 
Sections: 'section SectionName'. 
Tasks: 'TaskName :done, crit, active, a1, YYYY-MM-DD, YYYY-MM-DD'. 
Milestones: 'MilestoneName :milestone, m1, YYYY-MM-DD'.

Entity Relationship Diagrams: 'erDiagram'. 
Entities: 'ENTITY_NAME { ... }'. 
Relationships: '--|{', '}--', '}o--', '--o{', '}--|{', '}--o{', '--o|{'.

Pie Charts: 'pie'. 
Data: 'title Pie Title', '"Label" : value'.

Git Graphs: 'gitGraph'. 
Branches, Commits: 'branch newbranch', 'commit', 'checkout', 'merge'.
"""


def mermaid(code: str) -> None:
    components.html(
        f"""
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """
    )

def mermaidCode(explaination, api_key):
    flowchart = palmAPI(api_key, f"Convert this explanation to a 'mermaid flowchart'  and make sure you follow these rules {mermaid_rules} too  : {explaination}")
    return flowchart




def show(api_key=None):
    st.title("Code Explainer")
    if api_key:
        exampleCode = st.text_area("Enter your code here")
        
        # Trigger codeExplainer only if exampleCode is not empty
        if exampleCode:
            explaination = codeExplainer(exampleCode, api_key)
            st.session_state['example_code'] = exampleCode
            st.write(explaination)
            st.write("Visual Explanation: ")
            st.write(mermaidCode(explaination, api_key))
            mermaid(mermaidCode(explaination, api_key))
    else:
        st.warning("Please enter your API key in the sidebar to access this feature.")
        



