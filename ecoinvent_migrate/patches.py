TECHNOSPHERE_PATCHES = {
    ("3.9.1", "3.10"): {
        "replace": [
            {
                "source": {
                    "name": "modified Solvay process, Hou's process",
                    "location": "GLO",
                    "reference product": "ammonium chloride",
                    "unit": "kg",
                },
                "target": {
                    "name": "soda ash production, dense, Hou's process",
                    "location": "GLO",
                    "reference product": "ammonium chloride",
                    "unit": "kg",
                },
            },
            {
                "source": {
                    "name": "Mannheim process",
                    "location": "RER",
                    "reference product": "sodium sulfate, anhydrite",
                    "unit": "kg",
                },
                "target": {
                    "name": "hydrochloric acid production, Mannheim process",
                    "location": "RER",
                    "reference product": "sodium sulfate, anhydrite",
                    "unit": "kg",
                },
            },
            {
                "source": {
                    "name": "Mannheim process",
                    "location": "RoW",
                    "reference product": "sodium sulfate, anhydrite",
                    "unit": "kg",
                },
                "target": {
                    "name": "hydrochloric acid production, Mannheim process",
                    "location": "RoW",
                    "reference product": "sodium sulfate, anhydrite",
                    "unit": "kg",
                },
            },
            {
                "source": {
                    "name": "wheat production, Swiss integrated production, intensive",
                    "location": "CH",
                    "reference product": "straw",
                    "unit": "kg",
                },
                "target": {
                    "name": "wheat grain production, Swiss integrated production, intensive",
                    "location": "CH",
                    "reference product": "straw",
                    "unit": "kg",
                },
            },
            {
                "source": {
                    "name": "wheat production, Swiss integrated production, extensive",
                    "location": "CH",
                    "reference product": "straw",
                    "unit": "kg",
                },
                "target": {
                    "name": "wheat grain production, Swiss integrated production, extensive",
                    "location": "CH",
                    "reference product": "straw",
                    "unit": "kg",
                },
            },
        ]
    }
}
