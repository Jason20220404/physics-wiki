---
type: source-original
immutable: true
status: draft
provenance: source-backed
source_pdf: sakurai-mqm-p29-31.pdf
printed_pages: "6-8"
extractor: pymupdf-1.24.11
anchor_scheme: "^pNN-sMM = paragraph NN, sentence MM (document-wide; running heads, headings, figure text, captions, footnotes are their own numbered blocks); ^eq-N-NN = display equation (N.NN), region kept as raw extraction — equation ground truth is the page images raw/sakurai-mqm-p29-31-pNN.png"
created: 2026-07-08
---

6 Fundamental Concepts ^p01-s01

experimental techniques we cannot make the Sz−component out of the third apparatus in Figure 1.3c disappear. ^p02-s01

The peculiarities of quantum mechanics are imposed upon us by the experiment itself. ^p02-s02

The limitation is, in fact, inherent in microscopic phenomena. ^p02-s03

1.1.3 Analogy with Polarization of Light ^p03-s01

Because this situation looks so novel, some analogy with a familiar classical situation may be helpful here. ^p04-s01

To this end we now digress to consider the polarization of light waves. ^p04-s02

This analogy will help us develop a mathematical framework for formulating the postulates of quantum mechanics. ^p04-s03

Consider a monochromatic light wave propagating in the z-direction. ^p05-s01

A linearly polarized (or plane polarized) light with a polarization vector in the x-direction, which we call for short an x-polarized light, has a space-time dependent electric ﬁeld oscillating in the x-direction ^p05-s02

E = E0ˆx cos(kz−ωt).
(1.5) ^eq-1-5

Likewise, we may consider a y-polarized light, also propagating in the z-direction, ^p05-s03

E = E0ˆy cos(kz−ωt).
(1.6) ^eq-1-6

Polarized light beams of type (1.5) or (1.6) can be obtained by letting an unpolarized light beam go through a Polaroid ﬁlter. ^p05-s04

We call a ﬁlter that selects only beams polarized in the x-direction an x-ﬁlter. ^p05-s05

An x-ﬁlter, of course, becomes a y-ﬁlter when rotated by 90◦about the propagation (z) direction. ^p05-s06

It is well known that when we let a light beam go through an x-ﬁlter and subsequently let it impinge on a y-ﬁlter, no light beam comes out provided, of course, we are dealing with 100% efﬁcient Polaroids; see Figure 1.4a. ^p05-s07

The situation is even more interesting if we insert between the x-ﬁlter and the y-ﬁlter yet another Polaroid that selects only a beam polarized in the direction – which we call the x′-direction – that makes an angle of 45◦with the x-direction in the xy plane; see Figure 1.4b. ^p06-s01

x-filter x-filter x -filter y-filter y-filter No beam (45° diagonal) 100% (a) (b) No light ^p07-s01

Fig. 1.4 Light beams subjected to Polaroid filters. ^p08-s01

7 1.1 The Stern–Gerlach Experiment ^p09-s01

y x yˆ xˆ yˆ xˆ y x ^p10-s01

Fig. 1.5 Orientations of the x′- and y′-axes. ^p11-s01

This time, there is a light beam coming out of the y-ﬁlter despite the fact that right after the beam went through the x-ﬁlter it did not have any polarization component in the y-direction. ^p12-s01

In other words, once the x′-ﬁlter intervenes and selects the x′-polarized beam, it is immaterial whether the beam was previously x-polarized. ^p12-s02

The selection of the x′-polarized beam by the second Polaroid destroys any previous information on light polarization. ^p12-s03

Notice that this situation is quite analogous to the situation that we encountered earlier with the SG arrangement of Figure 1.3b, provided that the following correspondence is made: ^p12-s04

Sz ±atoms ↔x-, y-polarized light
Sx ±atoms ↔x′-, y′-polarized light,
(1.7) ^eq-1-7

where the x′- and the y′-axes are deﬁned as in Figure 1.5. ^p12-s05

Let us examine how we can quantitatively describe the behavior of 45◦-polarized beams (x′- and y′-polarized beams) within the framework of classical electrodynamics. ^p13-s01

Using Figure 1.5 we obtain ^p13-s02

E0ˆx′ cos(kz−ωt) = E0
 1
√
2
ˆxcos(kz−ωt)+ 1
√
2
ˆycos(kz−ωt)

,
E0ˆy′ cos(kz−ωt) = E0

−1
√
2
ˆxcos(kz−ωt)+ 1
√
2
ˆycos(kz−ωt)

.
(1.8) ^eq-1-8

In the triple-ﬁlter arrangement of Figure 1.4b the beam coming out of the ﬁrst Polaroid is an ˆx-polarized beam, which can be regarded as a linear combination of an x′-polarized beam and a y′-polarized beam. ^p13-s03

The second Polaroid selects the x′-polarized beam, which can in turn be regarded as a linear combination of an x-polarized and a y-polarized beam. ^p13-s04

And ﬁnally, the third Polaroid selects the y-polarized component. ^p13-s05

8 Fundamental Concepts ^p14-s01

Applying correspondence (1.7) from the sequential Stern–Gerlach experiment of Figure 1.3c, to the triple-ﬁlter experiment of Figure 1.4b suggests that we might be able to represent the spin state of a silver atom by some kind of vector in a new kind of two-dimensional vector space, an abstract vector space not to be confused with the usual two-dimensional (xy) space. ^p15-s01

Just as ˆx and ˆy in (1.8) are the base vectors used to decompose the polarization vector ˆx′ of the ˆx′-polarized light, it is reasonable to represent the Sx+ state by a vector, which we call a ket in the Dirac notation to be developed fully in the next section. ^p15-s02

We denote this vector by |Sx; +⟩and write it as a linear combination of two base vectors, |Sz; +⟩and |Sz; −⟩, which correspond to the Sz+ and the Sz−states, respectively. ^p15-s03

So we may conjecture ^p15-s04

|Sx; +⟩
?= 1
√
2
|Sz; +⟩+ 1
√
2
|Sz; −⟩
(1.9a) ^eq-1-9a

|Sx; −⟩
?= −1
√
2
|Sz; +⟩+ 1
√
2
|Sz; −⟩
(1.9b) ^eq-1-9b

in analogy with (1.8). ^p15-s05

Later we will show how to obtain these expressions using the general formalism of quantum mechanics. ^p15-s06

Thus the unblocked component coming out of the second (SGˆx) apparatus of Figure 1.3c is to be regarded as a superposition of Sz+ and Sz−in the sense of (1.9a). ^p16-s01

It is for this reason that two components emerge from the third (SGˆz) apparatus. ^p16-s02

The next question of immediate concern is: How are we going to represent the Sy± states? ^p17-s01

Symmetry arguments suggest that if we observe an Sz± beam going in the x-direction and subject it to an SGˆy apparatus, the resulting situation will be very similar to the case where an Sz± beam going in the y-direction is subjected to an SGˆx apparatus. ^p17-s02

The kets for Sy± should then be regarded as a linear combination of |Sz; ±⟩, but it appears from (1.9) that we have already used up the available possibilities in writing |Sx; ±⟩. ^p17-s03

How can our vector space formalism distinguish Sy± states from Sx± states? ^p17-s04

An analogy with polarized light again rescues us here. ^p18-s01

This time we consider a circularly polarized beam of light, which can be obtained by letting a linearly polarized light pass through a quarter-wave plate. ^p18-s02

When we pass such a circularly polarized light through an x-ﬁlter or a y-ﬁlter, we again obtain either an x-polarized beam or a y-polarized beam of equal intensity. ^p18-s03

Yet everybody knows that the circularly polarized light is totally different from the 45◦-linearly polarized (x′-polarized or y′-polarized) light. ^p18-s04

Mathematically, how do we represent a circularly polarized light? ^p19-s01

A right circularly polarized light is nothing more than a linear combination of an x-polarized light and a y-polarized light, where the oscillation of the electric ﬁeld for the y-polarized component is 90◦out of phase with that of the x-polarized component:4 ^p19-s02

E = E0
 1
√
2
ˆxcos(kz−ωt)+ 1
√
2
ˆycos

kz−ωt+ π
2

.
(1.10) ^eq-1-10

4 Unfortunately, there is no unanimity in the deﬁnition of right versus left circularly polarized light in the literature. ^p20-s01
