# Chassis Operations Platform

A sanitized portfolio adaptation of an operational solution that combines vehicle-location lookup, event history, transfer context, list synchronization and dispatch-document support.

## Problem

Vehicle location and movement context were spread across operational sources. Users needed a fast lookup surface while background processes had to normalize snapshots, plan list changes, preserve history and avoid unsafe bulk updates.

## Solution

The private solution combines a Power Apps Canvas application, a list synchronization service, an event-history layer, transfer data and document automation. This public repository preserves the proven component boundaries but replaces every source with local synthetic CSV files. It can build a dry-run plan; it cannot authenticate or write externally.

## Architecture

```text
Incoming snapshot ─> normalize ─> compare ─> guarded dry-run plan
                                         ├─> location registry
                                         └─> event history

Transfer requests ──────────────────────────> Power Apps views
Dispatch document metadata ─────────────────> Power Apps views
```

See [solution overview](docs/solution-overview.md), [data model](docs/data-model.md) and [security boundaries](docs/security-boundaries.md).

## Main components

- **Chassis Tracker App:** documented Canvas app for search, status, location and history.
- **List Sync Service:** local normalization, comparison, dry-run planning and guardrail checks.
- **Event History Layer:** derives auditable events from planned changes.
- **Transfer Data Integration:** models origin and destination requests.
- **Dispatch Document Automation:** produces explicitly marked synthetic document text.

## Repository structure

```text
src/chassis_platform/  local-only Python services
tests/                 pure behavior tests
sample-data/           invented snapshots and transfers
power-apps/            sanitized formulas and screen model
docs/                  architecture, data and security notes
site/                  GitHub Pages case study
```

## Technologies

Python standard library, CSV/JSON, pytest, ruff, Power Fx documentation, semantic HTML/CSS and GitHub Actions. SharePoint, browser automation, Power Apps connections and external spreadsheet sources are private and not implemented here.

## Run with synthetic data

```bash
python -m venv .venv
python -m pip install -e .
python -m chassis_platform.cli
```

The command writes a local dry-run plan under `output/`, which Git ignores. It performs zero external writes.

## Security and anonymization

Identifiers use the `DEMO` prefix. Locations, dates and requests are fictional. Original MSAPP files, spreadsheets, PDFs, outputs, profiles, logs, executables, credentials, URLs and list names are excluded. See [PUBLIC_RELEASE_AUDIT.md](PUBLIC_RELEASE_AUDIT.md).

## Limitations of the public version

- No MSAPP is shipped and the generic Power Fx is not import-ready.
- The production SharePoint and browser adapters remain private.
- Document output is plain synthetic text, not an original corporate template.
- Dry-run planning demonstrates control flow but does not publish changes.
- No operational performance claims or metrics are presented.

## Technical decisions

The local adapter makes the safe execution boundary visible. Sync planning is pure and reviewable; guardrails run before export; history is derived from changes; document generation is separate from list synchronization. External implementation belongs behind adapters that are deliberately absent.

## Next steps

- Add synthetic XLSX samples when the controlled workbook tool is available.
- Add screenshots recreated entirely from synthetic content.
- Define an optional connector protocol without publishing an environment-specific client.

## Author

Portfolio project maintained by the repository owner.

## Resumo em português

Versão pública e sanitizada de uma solução de localização de chassis, histórico de eventos, transferências, sincronização de listas e documentos. O exemplo executa apenas com CSVs fictícios, gera um plano local de dry-run e não possui credenciais nem capacidade de escrita corporativa.

