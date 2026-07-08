---
type: ref
status: draft            # not yet reviewed-by-me
provenance: mixed        # derivation [A]; grounding [unverified]
saturation_depth: 1
created: 2026-07-06
sources: []              # raw/ has no supporting source yet — deliberately exposed
---

# U = −μ·B — magnetic dipole potential energy

> An **explication (de-compression)** page. It unfolds the textbook one-liner `U = −μ·B`
> into prerequisites → step derivation (with joints) → grounding → open questions, and
> marks the identity of every claim. Joints are clickable: `saturate Jnn` to expand one.

## 0. The question this page answers
When you see `U = −μ·B`: where does the minus sign come from? why a dot product? what
experiment is it grounded on?

## 1. Prerequisites
- [[ref/magnetic-moment]] — μ = I·A (current loop)  `[A]`  *(to build)*
- [[ref/torque-on-current-loop]] — τ = μ × B  `[A]`  *(to build)*
- rotational potential energy: τ = −dU/dθ  `[A]`
- dot product geometry: a·b = |a||b|cosθ  `[A]`

## 2. Step derivation  `[A]` (every step checkable against a textbook)
1. In uniform **B**, moment **μ** feels torque `τ = μ × B`, magnitude `τ = μB·sinθ`. ⟨J01:[A]⟩⟨J02:?⟩
2. Define potential energy so the aligning torque is its negative gradient: `τ = −dU/dθ`. ⟨J03:[A]⟩
3. Integrate, reference `U(90°)=0`:  `U(θ) = −μB·cosθ`. ⟨J04:[A]⟩
4. Write geometry back as a dot product: `μB·cosθ = μ·B`, so **`U = −μ·B`**. ∎ ⟨J05:?⟩

**Physical check:** θ=0 (μ ∥ B) → U=−μB (lowest, stable); θ=180° → U=+μB (highest). ✔

## 3. Grounding / empirical basis  ⚠️ HIGHEST SCRUTINY
> All historical/experimental attributions are `[unverified: model-knowledge]`: no first-hand
> source in `raw/` yet. Per schema, anchor before use.
- **Stern–Gerlach (I recall 1922)** `[unverified]` — silver-atom beam splits into discrete
  beams in an inhomogeneous field; grounds the μ·B interaction + space quantization.
- **Zeeman effect (I recall 1896)** `[unverified]` — spectral lines split in a field; level
  shift ∝ μ·B.
- **Classical side** `[unverified]` — torque on a current loop, back to Ampère-era work.

> `Spark, don't settle`: I do not decide *which* experiment is "the" foundation. That is your
> call after reading a first-hand source; it goes to `think/`.

---

## Saturated joints
> Expanded on click, at `saturation_depth: 1` (one layer, then stop). Sub-joints stay `?`.

### ⟨J01:[A]⟩ — τ = μ × B  · type: derivational
A planar current loop (μ = IA) in uniform B: each element feels `dF = I dL × B`; integrated
around the loop the net force is zero but the net torque collects to `τ = μ × B`.  `[A]`
↳ spawned: ⟨J01.1:?⟩ dF = I dL × B (→ Lorentz force) · ⟨J01.2:?⟩ μ = IA (**conventional**, bedrock candidate) · ⟨J01.3:?⟩ why the loop integral yields exactly μ×B (geometry)

### ⟨J03:[A]⟩ — τ = −dU/dθ  · type: **conventional wrapping a derivational premise** (tangled)
- *Conventional half:* `τ = −dU/dθ` is the **defining relation** of potential energy; the minus
  sign is a **sign convention** (chosen so U is minimal where the torque vanishes). No "because" —
  it is a stipulation.
- *Derivational half (load-bearing, easily missed):* this definition is only **available** because
  the aligning torque is **conservative** — else no single-valued U(θ) exists.
↳ spawned: ⟨J03.1:?⟩ the torque is conservative, ∮τ dθ = 0 (**derivational**, the real physics) · ⟨J03.2:?⟩ the sign convention (**conventional**, bedrock candidate)

### ⟨J04:[A]⟩ — reference U(90°)=0  · type: **conventional** (pure choice)
No physical reason — **it is a choice.** Any reference shifts U by a constant; physics depends
only on dU (force, torque), never on U's absolute value, so the reference never touches an
observable. Picking θ=90° merely makes the result collect cleanly to `−μ·B` — that is
*convenience, not fact.* Natural **bedrock `▣`** candidate on your approval.

---

## Open joint map (unexpanded — your handles)
`⟨J02:?⟩` |τ|=μB·sinθ (derivational, near-definition, bedrock candidate)
`⟨J05:?⟩` μB·cosθ = μ·B (derivational, definition, bedrock candidate)
`⟨J01.1:?⟩ ⟨J01.2:?⟩ ⟨J01.3:?⟩ ⟨J03.1:?⟩ ⟨J03.2:?⟩`

*log: `## [2026-07-06] explicate | U = −μ·B` · `saturate J01, J03, J04`*
