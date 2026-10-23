---
title: Domain model
status: draft
updated: 2026-10-23
---

# Domain model

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "ordered as"
```

<!-- Placeholder example: replace with the real model during /system-analysis. -->
