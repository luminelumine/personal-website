# Lessons Learned

## Patterns to Follow

### Portfolio information architecture
- **Pattern:** Use category labels such as `Selected Work` on the personal homepage instead of exposing an individual product name as a top-level act.
- **Why:** This preserves the homepage's editorial structure and supports future projects.

### Case-study restraint
- **Pattern:** Keep the Polara case study to three major sections and fold implementation proof into the narrative.
- **Why:** The personal website is intentionally minimal; many small sections make the page feel like a presentation deck.

### Evidence placement
- **Pattern:** Do not place early seed-user or social-engagement metrics on the Selected Work index.
- **Why:** The index should communicate project identity, role, and scope without overstating early promotional signals.

### Product facts
- **Pattern:** Use `100+ pole tricks` in current portfolio copy.
- **Why:** The founder confirmed this as the current public-facing product scale; do not reuse the older repository count.

### Design-system fidelity
- **Pattern:** Before designing a new portfolio page, visually audit at least two existing subpages and reuse their actual shell, typography roles, spacing, borders, and interaction language.
- **Why:** A page can reuse a font family but still feel foreign when it assigns that font a new role or introduces an unrelated editorial layout.

### Product imagery
- **Pattern:** Use the founder-supplied current App Store exports and simulator screenshots as the canonical Polara imagery; verify the exact source path before composing a preview.
- **Why:** Rebuilding or substituting device mockups makes the product look inconsistent and can surface stale UI or outdated trick counts.

### App Store screenshot legibility
- **Pattern:** Show tall App Store marketing screenshots at their full aspect ratio whenever their embedded headlines are part of the story; do not use `object-fit: cover` in a short landscape viewport.
- **Why:** Cover-cropping preserves visual impact but removes the marketing copy and makes the screenshots look broken rather than intentionally framed.

### Brand integration
- **Pattern:** Let a featured product contribute accent color and imagery while the portfolio's existing typography and page shell stay dominant.
- **Why:** The work should feel selected by the portfolio, not like a separate marketing site embedded inside it.

### Responsive interaction consistency
- **Pattern:** When the same image gallery appears across responsive sizes, preserve its interaction direction unless the layout creates a clear usability constraint.
- **Why:** Switching a horizontal gallery to vertical only on desktop makes the component feel like a different experience and weakens the intended visual rhythm.

### Portfolio readability
- **Pattern:** Keep explanatory portfolio copy at a comfortably readable size and contrast; reserve very small, dim mono type for truly secondary metadata only.
- **Why:** The visual system can remain restrained without making the project story difficult to read, especially in the sidebar and case-study explanations.

### Product-story coverage
- **Pattern:** When current App Store screenshots already form a seven-frame product narrative, show the complete set in the case-study product rail.
- **Why:** Omitting frames hides useful product breadth and wastes finished launch-quality assets.

### Purposeful motion
- **Pattern:** Use motion to reveal hierarchy, communicate horizontal-gallery position, and reward interaction; always provide a reduced-motion path.
- **Why:** Motion should make the page easier to follow and feel more alive without becoming ornamental or competing with the product imagery.
