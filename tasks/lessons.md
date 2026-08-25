# Lessons Learned

## Patterns to Follow

### Portfolio information architecture
- **Pattern:** Use category labels such as `Selected Work` on the personal homepage instead of exposing an individual product name as a top-level act.
- **Why:** This preserves the homepage's editorial structure and supports future projects.

### Product-page restraint
- **Pattern:** Keep Polara on one product-first page, and add only sections that directly improve product understanding, search relevance, or provenance.
- **Why:** Inline demos and concise About/Methodology information help dancers and search systems without reviving a portfolio process deck or creating fragmented microsites.

### One public Polara page
- **Pattern:** Use the existing Polara page as the product landing page instead of maintaining a separate product page and case study.
- **Why:** App Store remains the download destination, while one product-first web page avoids duplicate content and duplicated maintenance.

### Evidence placement
- **Pattern:** Do not place early seed-user or social-engagement metrics on the Selected Work index.
- **Why:** The index should communicate project identity, role, and scope without overstating early promotional signals.

### Product facts
- **Pattern:** Use `100+ pole tricks` in current portfolio copy.
- **Why:** The founder confirmed this as the current public-facing product scale; do not reuse the older repository count.

### Protect the trick library
- **Pattern:** Keep Polara's complete trick library inside the app; public web content may show only Ballerina and Ayesha as representative demos, embedded in the product page rather than separate trick pages.
- **Why:** The library is a core product asset and publishing the full dataset would make it easy to copy. SEO should rely on strong product pages, original practitioner-led content, and a small illustrative demo rather than a crawlable replica of the database.

### Trick demo presentation
- **Pattern:** Present Search & Filter, Ballerina, and Ayesha as one compact horizontal card rail. Use the same split-copy/full-phone composition for each card, and never crop the status bar or lower controls. Omit level and theme labels from the web copy, and make the three progress states directly interactive.
- **Why:** A consistent right-scroll rail matches the established How It Works interaction, reduces page length, and keeps complete product screens legible without revealing more library content.

### Design-system fidelity
- **Pattern:** Before designing a new portfolio page, visually audit at least two existing subpages and reuse their actual shell, typography roles, spacing, borders, and interaction language.
- **Why:** A page can reuse a font family but still feel foreign when it assigns that font a new role or introduces an unrelated editorial layout.

### Product imagery
- **Pattern:** Use the founder-supplied current App Store exports and simulator screenshots as the canonical Polara imagery; verify the exact source path before composing a preview.
- **Why:** Rebuilding or substituting device mockups makes the product look inconsistent and can surface stale UI or outdated trick counts.

### App Store screenshot legibility
- **Pattern:** In the detailed case study, show tall App Store marketing screenshots at their full aspect ratio whenever their complete narrative is part of the story.
- **Why:** The case study has enough space for exhaustive screenshot coverage, so marketing copy should remain fully readable there.

### Editorial screenshot crops
- **Pattern:** When marketing narrative is the goal, a top-aligned cover crop can keep a primary headline whole and exclude secondary copy as a complete block.
- **Why:** This is cleaner than large gutters or half-visible marketing text, but it should not be used when the index needs to foreground the product interface.

### Product-led index imagery
- **Pattern:** When the portfolio index is meant to demonstrate the product, position branded App Store artwork around the phone UI and let marketing headlines leave the frame.
- **Why:** Marketing typography can overpower a compact project card; screen-first crops show more design and engineering evidence while retaining the product's visual world.

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
