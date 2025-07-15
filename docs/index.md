# The Finisher's Signature: A Data-Driven Analysis of Messi vs. Mbappé  
*A project by [Clarkey33](https://www.linkedin.com/in/your-link-here)*

---

## Introduction

In football, the goal count is king. But what if it’s lying to us?

Raw goal totals tell only part of the story. They ignore context—shot difficulty, defensive pressure, or angle. In the modern analytics era, that’s not enough. To understand *how* great a finisher really is, we must ask: **Are they consistently scoring more than they should?**

This project sets out to do just that. By building a custom Expected Goals (xG) model, we go beyond the highlight reels to quantify finishing skill with precision. Our focus: two generational forwards—**Lionel Messi and Kylian Mbappé**.

---

## The Verdict: Consistent, Elite Overperformance

Using four years of publicly available FBRef data, the findings are unambiguous: both players are elite finishers, consistently outperforming expected goals. 

- **Kylian Mbappé:** +18 Goals Above Expected (G-xG)
- **Lionel Messi:** +5.4 Goals Above Expected (G-xG)

This means that, compared to a league-average player taking the same shots, both have delivered *more* goals—and by margins that aren’t due to chance.

![Stacked bar chart of Messi vs. Mbappé G-xG](https://github.com/Clarkey33/xG-model/blob/main/images/player_finishing_profile/2021-2025_G%20-xG_messi_mbappe_performance.png?raw=true)

---

## The Deeper Story: Uncovering Finishing Signatures

While both overperform, *how* they do so is where it gets fascinating.

By comparing our custom xG model to StatsBomb’s industry benchmark, we reveal two distinct **finishing archetypes**. These aren't just statistical quirks—they are signatures, shaped by style, situation, and skillset.

![Mbappé vs. Messi xG scatter plots](https://github.com/Clarkey33/xG-model/blob/main/images/player_finishing_profile/mbappe_shot_xG_predicted_xG.png?raw=true)  
![Messi vs. Mbappé xG scatter plots](https://github.com/Clarkey33/xG-model/blob/main/images/player_finishing_profile/messi_shot_xG_predicted_xG.png?raw=true)

---

## Deep Dive 1: Mbappé, The “Dynamic Finisher”

Mbappé's finishing profile is explosive, unpredictable—and nearly unmodelable.

The custom model systematically **undervalued** his chances. Why? Because it couldn't see what the eye can: breakneck sprints, instinctive shots, and finishes in chaotic, high-pressure moments. These are scenarios that demand more advanced tracking data to capture fully. Mbappé thrives in *motion*, and his goals often emerge from volatility.

![Mbappé shot map](https://github.com/Clarkey33/xG-model/blob/main/images/Mbappe/shot_map.png?raw=true)

---

## Deep Dive 2: Messi, The “Technical Maestro”

Messi, on the other hand, plays geometry.

Where the models agreed, Messi succeeded—creating shot opportunities that are mathematically clean, technically optimal, and beautifully engineered. His shot map suggests a player who manipulates space with clinical precision. Unlike Mbappé’s chaos, Messi’s brilliance lies in control.

![Messi shot map](https://github.com/Clarkey33/xG-model/blob/main/images/Messi/shot_map.png?raw=true)

---

## Watch the Full Presentation

Want the full walkthrough, visuals, and explanation of the methodology?

[![Watch the video](https://www.youtube.com/watch?v=4pMvgw1hn94)]

---

## Dive Deeper

- 📄 [Read the full PDF report](https://github.com/Clarkey33/xG-model/blob/main/report/player_finishing_profile_report.pdf)
- 💻 [Explore the GitHub repository: Clarkey33/xG-model](https://github.com/Clarkey33/xG-model)  
  *Build an Expected Goals (xG) model from scratch using StatsBomb’s FIFA World Cup 2022 dataset. Data cleaning, feature engineering (shot angle & distance), and visualization included.*

---
