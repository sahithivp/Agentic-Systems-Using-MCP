from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluator(simulation_result: str):
    prompt = f"""
You are an expert molecular modeler and computational biophysics evaluator.

Your task is to critically evaluate the following docking or simulation result
and provide a structured, rigorous scientific assessment:

--- Simulation Result ---
{simulation_result}
--- End ---

### Your Evaluation Must Include:

1. **Scientific Validity**
   - Are the docking poses, interactions, and energies plausible?
   - Are there methodological red flags or missing details?

2. **Binding Interaction Analysis**
   - Identify key residues, hydrogen bonds, hydrophobic contacts, ionic interactions.
   - Evaluate binding pocket fit and stability.

3. **Energetic & Structural Assessment**
   - Interpret binding affinity values.
   - Assess conformational strain, clashes, or unrealistic geometries.

4. **Potential Issues or Contradictions**
   - Note inconsistencies, errors, or missing parameters.
   - Flag if the result seems artificially inflated or unreliable.

5. **Refinement Suggestions**
   - Suggest specific methodological improvements such as:
       • re-docking with different parameters  
       • performing MD simulations  
       • improving ligand protonation/geometry  
       • sampling alternative binding modes  
       • improving scoring/rescoring  
   - Make suggestions actionable, step-wise, and technical.

6. **Confidence Score (0–100%)**
   - How confident are you in your evaluation?

Provide your answer in the following format:

---
**Evaluation**
[content]

**Recommended Refinements**
[content]

**Confidence Score:** X%
---
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
