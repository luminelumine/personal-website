# Polara Index Safe Cover

## Goal

Restore the strong, full-bleed scale of the Selected Work gallery without leaving partial marketing headlines at the crop boundary.

## Approved Design

- Use `object-fit: cover` so each App Store screenshot fills the media pane.
- Align the artwork to the top. The primary headline remains complete and the product UI extends naturally beyond the lower frame edge.
- Allow secondary copy blocks to sit entirely outside the frame. Never leave a partial marketing headline visible at an edge.
- Keep the existing horizontal gallery, counter, card proportions, and Polara color treatment.
- Do not add vertical scrolling or image-internal panning.

## Responsive Behaviour

- Desktop, tablet, and mobile use the same top-aligned editorial crop.
- The gallery continues to scroll horizontally and snap one frame at a time.
- The compact mobile counter remains so it does not cover the primary headline.

## Verification

- Inspect every frame at desktop and mobile sizes.
- Confirm the primary headline is complete on headline-led frames.
- Confirm no secondary marketing headline is partially visible at the bottom edge.
- Confirm gallery scrolling, counter updates, loading, and page overflow remain correct.

## Superseded Design

This replaces `2026-08-21-polara-index-screenshot-fit-design.md`. Full-image containment was legible but made the artwork feel too small and left excessive gutters.
