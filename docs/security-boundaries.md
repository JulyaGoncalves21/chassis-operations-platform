# Security boundaries

- Local CSV is the only implemented source.
- The code contains no HTTP client, browser automation, credential store or SharePoint writer.
- `.env.example` exposes variable names only; all values are empty or generic.
- Original MSAPP, YAML sources, environment/application/tenant IDs, list names and connector metadata remain private.
- Original documents, PDFs, spreadsheets, outputs, evidence, logs and browser profiles remain private.
- A sync plan is not an authorization to execute changes. The public CLI only exports the plan.

