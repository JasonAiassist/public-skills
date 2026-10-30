# XML and MSBuild project files
Baseline: [W3C XML 1.0](https://www.w3.org/TR/xml/) and the repository's existing MSBuild conventions.
- Keep documents well formed, preserve namespaces and element ordering when those affect the consumer, and use UTF-8 unless the file declares another encoding.
- Escape XML special characters in values. Treat external XML as untrusted; disable DTD and external entity resolution in new parsers unless explicitly required.
- Make narrow changes to project properties and package pins. Avoid reformatting unrelated XML or changing build conditions without checking affected target frameworks.
- Validate with the project-native restore/build or parser and inspect the changed file diff. Confirm resolved package versions and any security audit result when changing dependencies.
