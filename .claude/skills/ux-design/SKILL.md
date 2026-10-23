---
name: ux-design
description: Design Sada's user experience and interface (information architecture, user flows, wireframes, screen specs, clickable HTML prototypes, usability test plans) in docs/05-ux-ui, using the design system tokens.
argument-hint: "<flow, screen, or story ID>"
---

# UX/UI design

Input: `$ARGUMENTS`. Read the related user stories, personas, `brand/voice-and-tone.md`, and
`design-system/` first.

1. **IA:** keep `information-architecture.md` current (sitemap as Mermaid, navigation model).
2. **Flow:** `flows/<flow>.md`: Mermaid flowchart covering the happy path, errors, and edge cases,
   linked to `US-###`.
3. **Wireframes:** low-fi HTML in `wireframes/<flow>/` (mobile first), greyscale.
4. **Screen specs:** `ui/SCR-###-slug.md` from `templates/ux/screen.md`: layout, components from
   `design-system/components/`, all states, final copy in brand voice, a11y notes, analytics events.
   Add the `SCR` to the story's `screens:` list.
5. **Prototype (optional):** a clickable hi-fi HTML prototype using the token values, published
   as an Artifact for stakeholder feedback.
6. **Test:** `usability-tests/<flow>-plan.md` with 5 tasks and success criteria; after testing,
   record findings with severity and the design changes made.
7. New components needed → run `/design-system`.
