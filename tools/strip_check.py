# -*- coding: utf-8 -*-
"""strip_check.py — the mechanical diff of CLAUDE.md §1a.

Verifies that a working copy (ref/<name>.md) is derived from its sealed
original (raw/<name>-original.md) by EXACTLY the two legal transforms:

  T1  wrapping existing words in [[target|<original words>]]
      (adds bracket/target characters, changes no displayed word);
  T2  replacing each garbled extracted-equation region with a $$...$$ block
      plus its trailing tag line ( `(N.NN)` [+ optional joint wikilink]
      + `[A]/[S?]/[S]·pNN` image pointer ).

Definition implemented here:

  PROSE(original) = original minus frontmatter, minus every ^eq-* unit,
                    minus the ' ^pNN-sMM' anchors  -> ordered list of
                    sentence lines.
    (The original is a sequence of anchored units: every unit ends on a line
     whose last token is ^pNN-sMM or ^eq-N-NN. A ^p unit is one sentence on
     one line; a ^eq unit is the verbatim garbled equation region.)

  STRIP(working)  = working minus frontmatter; every $$...$$ block AND its
                    REQUIRED trailing tag line excised; every
                    [[target|display]] wikilink unwrapped to 'display';
                    blank lines dropped  -> ordered list of sentence lines.

  PASS  <=>  the two lists are byte-identical, element by element.
             (Whitespace *layout* — blank-line grouping into paragraphs —
             is the only thing not compared; every sentence's bytes are.)

Any mismatch, a $$ block without a tag line, an unclosed $$, or a leftover
garbled-equation line in the working copy fails the check. Exit 0 = pass,
exit 1 = drift (first divergence reported). Nothing is ever written.

Usage:
    python tools/strip_check.py <raw/...-original.md> <ref/....md>
    python tools/strip_check.py            # defaults to sakurai-mqm-p29-31
"""
import io, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ANCHOR_RE = re.compile(r"\s\^(p\d{2}-s\d{2}|eq-[0-9a-z-]+)\s*$")
# tag line under a $$...$$ block: optional joint wikilink around (N.NN),
# then the identity tag + page-image pointer, optionally backticked.
TAG_RE = re.compile(
    r"^(?:\[\[[^|\]]+\|)?\(\d+\.\d+[a-z]?\)(?:\]\])?"   # (1.8) or [[...|(1.8)]]
    r"\s+`?\[(?:A|S\??)\]·p\d+`?\s*$"                    # `[A]·p30` etc.
)
WIKILINK_RE = re.compile(r"\[\[[^|\]]+\|([^\]]+)\]\]")


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    # strip YAML frontmatter
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[i + 1:]
        raise SystemExit("unterminated frontmatter in " + path)
    return lines


def prose_of_original(path):
    """Ordered sentence lines of the original (eq units skipped, anchors stripped)."""
    sentences, unit = [], []
    for ln in read_lines(path):
        unit.append(ln)
        m = ANCHOR_RE.search(ln)
        if not m:
            continue
        anchor = m.group(1)
        if anchor.startswith("eq-"):
            unit = []                       # discard the whole equation unit
            continue
        body = [l for l in unit if l.strip()]
        if len(body) != 1:
            raise SystemExit(
                "original %s: sentence unit ^%s is not a single line" % (path, anchor))
        sentences.append(ANCHOR_RE.sub("", body[0]))
        unit = []
    leftover = [l for l in unit if l.strip()]
    if leftover:
        raise SystemExit("original %s: trailing lines with no anchor: %r"
                         % (path, leftover[:3]))
    return sentences


def strip_working(path):
    """Apply STRIP: drop $$..$$ + tag line, unwrap wikilinks, drop blanks."""
    lines = read_lines(path)
    out, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        if ln.strip() == "$$":                      # T2 block begins
            j = i + 1
            while j < n and lines[j].strip() != "$$":
                j += 1
            if j >= n:
                raise SystemExit("working %s: unclosed $$ block at line %d"
                                 % (path, i + 1))
            k = j + 1
            while k < n and not lines[k].strip():   # skip blanks before tag
                k += 1
            if k >= n or not TAG_RE.match(lines[k].strip()):
                raise SystemExit(
                    "working %s: $$ block at line %d has no valid tag line "
                    "((N.NN) + [A]·pNN) — got: %r"
                    % (path, i + 1, lines[k].strip() if k < n else "<EOF>"))
            i = k + 1                               # excise block + tag line
            continue
        if ln.strip():
            out.append(WIKILINK_RE.sub(r"\1", ln))  # T1 unwrapped
        i += 1
    return out


def main():
    if len(sys.argv) == 3:
        orig, work = sys.argv[1], sys.argv[2]
    else:
        orig = r"D:\physics-wiki\raw\sakurai-mqm-p29-31-original.md"
        work = r"D:\physics-wiki\ref\sakurai-mqm-p29-31.md"

    a, b = prose_of_original(orig), strip_working(work)

    print("original sentence units :", len(a))
    print("working  sentence lines :", len(b))

    for idx in range(min(len(a), len(b))):
        if a[idx] != b[idx]:
            print("STRIP-CHECK FAIL at sentence %d" % (idx + 1))
            print("  original: %r" % a[idx])
            print("  working : %r" % b[idx])
            for c in range(min(len(a[idx]), len(b[idx]))):
                if a[idx][c] != b[idx][c]:
                    print("  first differing char at col %d: %r vs %r"
                          % (c + 1, a[idx][c], b[idx][c]))
                    break
            sys.exit(1)
    if len(a) != len(b):
        longer, name = (a, "original") if len(a) > len(b) else (b, "working")
        print("STRIP-CHECK FAIL: length mismatch — extra in %s:" % name)
        print("  %r" % longer[min(len(a), len(b))])
        sys.exit(1)

    print("STRIP-CHECK PASS — working copy is byte-identical to the sealed "
          "original under the two legal transforms")


if __name__ == "__main__":
    main()
