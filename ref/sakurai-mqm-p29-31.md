---
type: ref
status: draft
provenance: candidate
saturation_depth: 1
created: 2026-07-08
sources: ["sakurai-mqm-p29-31-original", "sakurai-mqm-p29-31.pdf"]
---

6 Fundamental Concepts

experimental techniques we cannot make the Sz−component out of the third apparatus in Figure 1.3c disappear.
The peculiarities of quantum mechanics are imposed upon us by the experiment itself.
The limitation is, in fact, inherent in microscopic phenomena.

1.1.3 Analogy with Polarization of Light

Because this situation looks so novel, some analogy with a familiar classical situation may be helpful here.
To this end we now digress to consider the polarization of light waves.
This analogy will help us develop a mathematical framework for formulating the postulates of quantum mechanics.

Consider a monochromatic light wave propagating in the z-direction.
A linearly polarized (or plane polarized) light with a polarization vector in the x-direction, which we call for short an x-polarized light, has a space-time dependent electric ﬁeld oscillating in the x-direction

$$
\mathbf{E} = E_0 \hat{\mathbf{x}} \cos(kz - \omega t).
$$
(1.5)  `[A]·p29`

Likewise, we may consider a y-polarized light, also propagating in the z-direction,

$$
\mathbf{E} = E_0 \hat{\mathbf{y}} \cos(kz - \omega t).
$$
(1.6)  `[A]·p29`

Polarized light beams of type (1.5) or (1.6) can be obtained by letting an unpolarized light beam go through a Polaroid ﬁlter.
We call a ﬁlter that selects only beams polarized in the x-direction an x-ﬁlter.
An x-ﬁlter, of course, becomes a y-ﬁlter when rotated by 90◦about the propagation (z) direction.
It is well known that when we let a light beam go through an x-ﬁlter and subsequently let it impinge on a y-ﬁlter, no light beam comes out provided, of course, we are dealing with 100% efﬁcient Polaroids; see Figure 1.4a.

The situation is even more interesting if we insert between the x-ﬁlter and the y-ﬁlter yet another Polaroid that selects only a beam polarized in the direction – which we call the x′-direction – that makes an angle of 45◦with the x-direction in the xy plane; see Figure 1.4b.

x-filter x-filter x -filter y-filter y-filter No beam (45° diagonal) 100% (a) (b) No light

Fig. 1.4 Light beams subjected to Polaroid filters.

7 1.1 The Stern–Gerlach Experiment

y x yˆ xˆ yˆ xˆ y x

Fig. 1.5 Orientations of the x′- and y′-axes.

This time, there is a light beam coming out of the y-ﬁlter despite the fact that right after the beam went through the x-ﬁlter it did not have any polarization component in the y-direction.
In other words, once the x′-ﬁlter intervenes and selects the x′-polarized beam, it is immaterial whether the beam was previously x-polarized.
The selection of the x′-polarized beam by the second Polaroid destroys any previous information on light polarization.
Notice that this situation is quite analogous to the situation that we encountered earlier with the SG arrangement of Figure 1.3b, provided that the following correspondence is made:

$$
\begin{aligned}
S_z \pm \text{ atoms} &\leftrightarrow x\text{-, } y\text{-polarized light} \\
S_x \pm \text{ atoms} &\leftrightarrow x'\text{-, } y'\text{-polarized light,}
\end{aligned}
$$
(1.7)  `[A]·p30`

where the x′- and the y′-axes are deﬁned as in Figure 1.5.

Let us examine how we can quantitatively describe the behavior of 45◦-polarized beams (x′- and y′-polarized beams) within the framework of classical electrodynamics.
Using Figure 1.5 we obtain

$$
\begin{aligned}
E_0 \hat{\mathbf{x}}' \cos(kz - \omega t) &= E_0 \left[ \frac{1}{\sqrt{2}} \hat{\mathbf{x}} \cos(kz - \omega t) + \frac{1}{\sqrt{2}} \hat{\mathbf{y}} \cos(kz - \omega t) \right], \\
E_0 \hat{\mathbf{y}}' \cos(kz - \omega t) &= E_0 \left[ -\frac{1}{\sqrt{2}} \hat{\mathbf{x}} \cos(kz - \omega t) + \frac{1}{\sqrt{2}} \hat{\mathbf{y}} \cos(kz - \omega t) \right].
\end{aligned}
$$
(1.8)  `[A]·p30`

In the triple-ﬁlter arrangement of Figure 1.4b the beam coming out of the ﬁrst Polaroid is an ˆx-polarized beam, which can be regarded as a linear combination of an x′-polarized beam and a y′-polarized beam.
The second Polaroid selects the x′-polarized beam, which can in turn be regarded as a linear combination of an x-polarized and a y-polarized beam.
And ﬁnally, the third Polaroid selects the y-polarized component.

8 Fundamental Concepts

Applying correspondence (1.7) from the sequential Stern–Gerlach experiment of Figure 1.3c, to the triple-ﬁlter experiment of Figure 1.4b suggests that we might be able to represent the spin state of a silver atom by some kind of vector in a new kind of two-dimensional vector space, an abstract vector space not to be confused with the usual two-dimensional (xy) space.
Just as ˆx and ˆy in (1.8) are the base vectors used to decompose the polarization vector ˆx′ of the ˆx′-polarized light, it is reasonable to represent the Sx+ state by a vector, which we call a ket in the Dirac notation to be developed fully in the next section.
We denote this vector by |Sx; +⟩and write it as a linear combination of two base vectors, |Sz; +⟩and |Sz; −⟩, which correspond to the Sz+ and the Sz−states, respectively.
So we may conjecture

$$
|S_x; +\rangle \overset{?}{=} \frac{1}{\sqrt{2}} |S_z; +\rangle + \frac{1}{\sqrt{2}} |S_z; -\rangle
$$
(1.9a)  `[A]·p31`

$$
|S_x; -\rangle \overset{?}{=} -\frac{1}{\sqrt{2}} |S_z; +\rangle + \frac{1}{\sqrt{2}} |S_z; -\rangle
$$
(1.9b)  `[A]·p31`

in analogy with (1.8).
Later we will show how to obtain these expressions using the general formalism of quantum mechanics.

Thus the unblocked component coming out of the second (SGˆx) apparatus of Figure 1.3c is to be regarded as a superposition of Sz+ and Sz−in the sense of (1.9a).
It is for this reason that two components emerge from the third (SGˆz) apparatus.

The next question of immediate concern is: How are we going to represent the Sy± states?
Symmetry arguments suggest that if we observe an Sz± beam going in the x-direction and subject it to an SGˆy apparatus, the resulting situation will be very similar to the case where an Sz± beam going in the y-direction is subjected to an SGˆx apparatus.
The kets for Sy± should then be regarded as a linear combination of |Sz; ±⟩, but it appears from (1.9) that we have already used up the available possibilities in writing |Sx; ±⟩.
How can our vector space formalism distinguish Sy± states from Sx± states?

An analogy with polarized light again rescues us here.
This time we consider a circularly polarized beam of light, which can be obtained by letting a linearly polarized light pass through a quarter-wave plate.
When we pass such a circularly polarized light through an x-ﬁlter or a y-ﬁlter, we again obtain either an x-polarized beam or a y-polarized beam of equal intensity.
Yet everybody knows that the circularly polarized light is totally different from the 45◦-linearly polarized (x′-polarized or y′-polarized) light.

Mathematically, how do we represent a circularly polarized light?
A right circularly polarized light is nothing more than a linear combination of an x-polarized light and a y-polarized light, where the oscillation of the electric ﬁeld for the y-polarized component is 90◦out of phase with that of the x-polarized component:4

$$
\mathbf{E} = E_0 \left[ \frac{1}{\sqrt{2}} \hat{\mathbf{x}} \cos(kz - \omega t) + \frac{1}{\sqrt{2}} \hat{\mathbf{y}} \cos\left( kz - \omega t + \frac{\pi}{2} \right) \right].
$$
(1.10)  `[A]·p31`

4 Unfortunately, there is no unanimity in the deﬁnition of right versus left circularly polarized light in the literature.
