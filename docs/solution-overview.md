# Solution overview

The original project contains multiple components rather than one script. The Canvas app is the user-facing lookup surface. A synchronization service prepares current location/status records. Changes feed an event-history layer. Transfer records provide origin/destination context, and a separate automation handles dispatch-document data.

The public package keeps these responsibilities separate. Only normalization, comparison, guardrails, event derivation and a synthetic document renderer are executable.

