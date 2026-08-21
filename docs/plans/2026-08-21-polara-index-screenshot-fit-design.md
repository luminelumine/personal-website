# Polara Index Screenshot Fit

## Goal

Keep the Selected Work card visually rich while making every headline and caption in the tall App Store screenshots visible.

## Approved Design

- Preserve the existing five-frame horizontal gallery, card proportions, typography, and interaction.
- Render each App Store screenshot at its complete aspect ratio with `object-fit: contain` instead of cropping it to fill the media pane.
- Use the existing Polara berry background behind the image so the necessary side gutters feel intentional.
- Remove screenshot-specific object-position overrides because a contained image does not need manual cropping.
- Keep the current hover response subtle and avoid enlarging the screenshot beyond its fitted bounds.

## Responsive Behaviour

- Desktop, tablet, and mobile keep the same horizontal scroll interaction.
- Each frame remains one media-pane width and scroll-snaps into place.
- The whole screenshot stays visible at every breakpoint without introducing page-level overflow.

## Verification

- Visually inspect the first and last frames at desktop and mobile sizes.
- Confirm all five screenshots retain their full top and bottom edges.
- Confirm horizontal scrolling, gallery count, lazy loading, and keyboard interaction still work.
- Confirm there are no console errors or page-level horizontal overflow.
