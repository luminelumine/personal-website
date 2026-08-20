# Polara Portfolio Design

**Date:** 2026-08-18
**Status:** Approved

## Objective

Add Polara to Lumine's personal website as both a portfolio case study and a lightweight product promotion page. The experience should help potential employers understand the end-to-end product work while allowing prospective users to understand and download the app quickly.

## Site Architecture

The homepage ticket gains a third category-level entry:

```text
ACT 03  >  SELECTED WORK
```

This opens a dedicated Selected Work index rather than linking directly to Polara. The index is designed to support additional projects later.

```text
Homepage
└── Selected Work
    └── Polara
```

## Selected Work Index

The index continues the website's near-black editorial and ticket-inspired visual language. Polara appears as the first large, horizontally composed project entry rather than as a generic card grid.

### Content

```text
SELECTED WORK
Products designed, built, and shipped independently.

01 / POLARA                                      2026
A private pole training companion for remembering
every trick and seeing progress over time.

ROLE
Independent Product Designer & Developer

SCOPE
Product Strategy · UX/UI · iOS · Monetization · Growth

[ VIEW CASE STUDY → ]
```

Do not show seed-user counts, social engagement, or an `Early Signal` block on the index.

### Visual Direction

- Preserve the existing serif and mono typography, near-black background, restrained borders, and editorial spacing.
- Introduce Polara's berry-pink accent only as a highlight.
- Use a real Polara product screen as the dominant visual.
- Add subtle image reveal or scale on hover.
- Keep project number `01` visible so the index can expand vertically.

## Polara Case Study

The page uses only three major sections. It should feel like one continuous editorial story rather than a series of presentation slides.

### 1. Hero

```text
POLARA
Never forget a trick.

A private iPhone companion for pole dancers to track
every trick, record practice, and see their progress.

[ DOWNLOAD ON THE APP STORE ]

ROLE
Independent Product Designer & Developer

SCOPE
Strategy · UX/UI · iOS · Brand · Monetization

100+ POLE TRICKS · 5 LEVELS · 3 LANGUAGES
```

The hero combines product promotion with portfolio context. Use a large iPhone product visual and transition the site's near-black background toward Polara's deep burgundy palette.

The App Store link remains available in the hero or sticky navigation. Do not add a separate closing CTA section.

### 2. The Product

Tell the product story through three connected real app screens rather than a feature inventory.

```text
REMEMBER → TRACK → REFLECT
```

- **Remember:** Search and keep every learned trick in one place.
- **Track:** Mark each trick as To Learn, Learning, or Landed.
- **Reflect:** Connect practice records into a visible personal journey.

### 3. The Thinking

Combine the problem, product insight, design decisions, and implementation context in one compact section.

```text
Pole dancers did not need another tutorial library.
They needed a personal memory for their pole journey.
```

Present three product decisions:

1. **Simple progress states** — Avoid complex scoring and let dancers define progress for themselves.
2. **Connected practice history** — Connect tricks, practice records, and progress over time.
3. **Private by design** — Use a local-first experience without a mandatory account, with user-controlled backup and restore.

End with one implementation line rather than another section:

```text
Designed and built independently with React Native,
Expo, TypeScript and StoreKit — from first idea to launch.
```

AI-assisted development may be acknowledged briefly within the process copy, but the primary role remains `Independent Product Designer & Developer`. Do not use `Vibe Coder` as the project title or role.

## Content Rules

- Keep the case study to exactly three major sections: Hero, Product, and Thinking.
- Use `100+ POLE TRICKS`, not the older `93 POLE TRICKS` figure.
- Do not present social likes or seed users as growth, impact, or product-market fit.
- Do not imply that Polara teaches technique, replaces instructors, or certifies safe execution.
- Do not claim automatic cloud sync; the product is local-first with user-controlled backup.
- Prefer real product screens and implemented facts over decorative feature claims.

## Responsive Behaviour

- On desktop, use asymmetrical editorial layouts with large product imagery.
- On mobile, stack text and product screens while retaining the Remember → Track → Reflect sequence.
- Keep the App Store action visible without duplicating a full CTA section.
- Preserve readable body copy and avoid shrinking mono labels below a comfortable mobile size.

## Success Criteria

- The homepage remains visually restrained and gains a scalable work category.
- A prospective user can understand Polara and find the App Store action from the first screen.
- A hiring reader can identify Lumine's role, product decisions, and implementation breadth without reading a long case study.
- The Polara page contains only three visually distinct major sections.
