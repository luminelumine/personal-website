# Changelog

All notable changes to this website are documented here.

## [0.1.0.0] - 2026-08-21

### Added

- Added a scalable Selected Work entry on the homepage and a dedicated project index.
- Added a three-part Polara case study covering the product, seven-screen product story, and key design decisions.
- Added responsive horizontal screenshot galleries, progress feedback, purposeful motion, and reduced-motion support.

### Changed

- Improved explanatory-copy readability, sidebar navigation, keyboard focus, touch targets, and responsive behavior.
- Replaced page-delivered screenshot PNGs with a 576 KB WebP set while retaining the original launch exports as source assets.
- Prepared the static site for clean Vercel publishing without local worktree files.

### Fixed

- Corrected Polara progress-state copy to match the shipped product.
- Added intrinsic image dimensions, lazy loading, and safe behavior when `IntersectionObserver` is unavailable.

### Removed

- Removed an unused draft stylesheet and four obsolete screenshots that were not part of the published experience.
