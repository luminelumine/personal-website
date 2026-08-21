# Project Tasks

## Current Sprint

- [ ] Replace contained Polara artwork with a safe full-bleed crop.
  - [x] Approve top-aligned cover treatment with whole primary headlines.
  - [ ] Implement the crop without vertical scrolling.
  - [ ] Inspect all five frames at desktop and mobile sizes.

- [x] Make Selected Work App Store screenshots fully readable.
  - [x] Diagnose the crop caused by the landscape media pane and `object-fit: cover`.
  - [x] Approve full-image `contain` treatment with Polara-colored gutters.
  - [x] Implement the responsive image-fit change.
  - [x] Verify desktop and mobile gallery behaviour and legibility.

- [ ] Publish the approved Polara portfolio work to luminetong.xyz.
  - [x] Confirm GitHub/Vercel deployment infrastructure and production domain.
  - [x] Run release checks.
  - [x] Create pull request #1.
  - [ ] Merge to main and wait for the Vercel production deployment.
  - [ ] Verify the production homepage, Selected Work index, and Polara gallery.

- [x] Inspect the personal website and Polara product context.
- [x] Define the Selected Work information architecture.
- [x] Approve the compact Polara case-study structure.
- [x] Audit the existing subpage design system and the supplied Polara screenshots.
- [x] Approve a design-system-native Selected Work index preview.
- [x] Approve a design-system-native Polara case-study preview.
- [x] Increase sidebar and explanatory-copy readability.
- [x] Expand the Product rail to all seven current App Store screenshots.
- [x] Add restrained, purposeful motion with reduced-motion support.
- [x] Implement the approved Selected Work index and Polara case study.
- [x] Verify desktop and mobile behaviour.

## Review Notes

- Approved structure: Homepage `Selected Work` entry → Selected Work index → Polara.
- Polara case study is limited to Hero, Product, and Thinking.
- The index does not show early-signal metrics.
- Existing subpages are the visual source of truth: Courier New, Modernline branding,
  dark ticket/card surfaces, 1px dividers, restrained uppercase metadata, and grain.
- Polara contributes official product imagery and a limited berry accent; it does not
  introduce a separate portfolio type system or page shell.
- The Selected Work screenshot rail scrolls horizontally at every responsive size.
- Sidebar navigation is 12px with 44px targets; explanatory copy is 16px with higher contrast.
- The Product rail contains all seven current App Store exports and remains horizontal at every breakpoint.
- Motion is limited to hero entrance, gallery progress feedback, hover response, and staggered Thinking reveals; reduced-motion users receive a static page.
- Final verification passed at 1440×900, 768×900, and 375×812 with no page-level horizontal overflow or console errors.
- Pre-landing review converged after removing dead assets, correcting product-state copy,
  optimizing the seven screenshots to a 576 KB WebP set, and adding accessible gallery fallbacks.
- Fresh browser QA passed the homepage → Selected Work → Polara path at desktop and mobile sizes;
  all galleries, lazy-loaded images, keyboard scrolling, counters, links, and console checks passed.
- The Selected Work gallery now preserves every App Store screenshot's full aspect ratio against
  the Polara berry background; its mobile counter is compact so it does not cover screenshot copy.
