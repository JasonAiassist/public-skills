# QML

Baseline: [Qt QML coding conventions](https://doc.qt.io/qt-6/qml-codingconventions.html), `qmlformat`, `qmllint`, and the host application's established components and imports.

- Order members consistently: `id`, properties, signals, JavaScript functions, object properties, then child objects. Use lower camel case for properties/functions and upper camel case for component files.
- Keep visual composition in QML and move reusable deterministic transformations into separately testable JavaScript or backend modules. Prefer property bindings and explicit signals over imperative synchronization.
- Treat values from processes, files, IPC, and network requests as untrusted. Parse defensively, validate expected types and bounds, and never build shell commands from user-controlled strings.
- Make asynchronous state explicit. Bound timers and process lifetimes, handle failure and cancellation, and avoid overlapping refresh jobs or retained signal connections.
- Preserve accessibility and keyboard navigation for interactive controls. Use theme-provided colours, spacing, typography, and icons rather than hard-coded substitutes when the host exposes them.
- Run `qmlformat` on changed QML where available and validate with `qmllint`. Use Qt Quick Test for reusable QML/JavaScript behaviour, plus a host-shell smoke check for integration that depends on application-specific imports.
