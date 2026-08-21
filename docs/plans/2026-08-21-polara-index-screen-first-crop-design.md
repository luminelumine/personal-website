# Polara Index Screen-First Crop

## Goal

Make the Selected Work gallery feel product-led by filling the media pane with the actual Polara interface rather than App Store marketing headlines.

## Approved Design

- Keep the existing five branded App Store images and the full-bleed `cover` treatment.
- Art-direct each frame around the phone screen:
  - Frames 1, 2, and 5 align to the bottom so their top marketing headlines leave the frame.
  - Frames 3 and 4 align to the top because their product UI occupies the upper section and their marketing slogans sit below it.
- Keep internal App UI text as product evidence, while minimizing external marketing copy.
- Keep the horizontal gallery and compact counter. Do not add vertical scrolling.

## Responsive Behaviour

- Use the same screen-first focal points on desktop and mobile.
- Retain the narrow-screen safe zoom on frame 4 if needed to prevent its lower marketing sentence from entering the crop.
- Do not introduce page-level overflow.

## Verification

- Inspect all five frames at desktop and mobile sizes.
- Confirm the dominant content in every frame is the phone screen.
- Confirm the large App Store marketing headlines are absent or visually negligible.
- Confirm horizontal scrolling, counter updates, image loading, and console state remain correct.

## Superseded Design

This replaces `2026-08-21-polara-index-safe-cover-design.md`, which preserved the marketing headlines but did not make the product interface dominant enough.
