Generate a comprehensive repository setup guide based on the AGENTS.md files in this repository.

Notes to agent:
- do not tool call to command line
- use the context given to you, especially AGENTS.md files
- read the root AGENTS.md and directory-specific AGENTS.md files
- reference the project structure shown in AGENTS.md files
- focus on creating a step-by-step setup guide that follows the patterns in AGENTS.md
- Do not make any code changes
- Do not include anything other than the output that the user will copy and paste
- never include emojis

Always wrap your output of the final setup guide EXACTLY as:
```markdown:./setup-guide.md
<your output>
```

The setup guide should include:

1. **Overview Section**
   - Purpose of the project (from root AGENTS.md)
   - Key principles mentioned in AGENTS.md files

2. **Prerequisites**
   - Required software and tools
   - Version requirements
   - Installation links if needed

3. **Project Structure**
   - Show the directory structure from AGENTS.md
   - Explain key directories and their purposes

4. **Setup Steps**
   - Backend setup (reference backend/AGENTS.md)
     - Configuration setup (pyproject.toml)
     - Business logic setup (src/)
     - API setup (app.py)
     - CLI setup (cli.py)
     - Testing setup
   - Frontend setup (reference frontend/AGENTS.md)
     - Package installation
     - Configuration
     - Component structure
   - Template customization (if applicable)
     - How to adapt for different domains
     - Reference customization sections

5. **Validation**
   - How to validate the setup
   - Reference validation scripts if mentioned

6. **Next Steps**
   - Running the application
   - Development workflow
   - Testing commands
   - Links to relevant AGENTS.md files for detailed instructions

The guide should be:
- Clear and actionable
- Follow the same structure as shown in AGENTS.md files
- Reference specific AGENTS.md files for detailed instructions
- Be suitable for someone setting up a new project from this template
- Include all necessary commands and file locations
- Maintain consistency with the educational/template nature of the project

Use imperative mood where appropriate (e.g., "Create", "Install", "Run").

