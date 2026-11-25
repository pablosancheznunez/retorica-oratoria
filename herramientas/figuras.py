"""Genera las figuras del libro (SVG) en figuras/.

Uso, desde la raíz del libro:   python3 herramientas/figuras.py [--png]
Paleta categórica validada (orden fijo): azul, naranja, aguamarina, amarillo, magenta.
"""
import pathlib, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

RAIZ = pathlib.Path(__file__).resolve().parent.parent
OUT = RAIZ / "figuras"; OUT.mkdir(exist_ok=True)

S = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
TINTA, TINTA2, GRIS, SUP = "#0b0b0b", "#52514e", "#d9d8d4", "#ffffff"
CAJA, CAJA2 = "#eef0f6", "#c9cfe0"

plt.rcParams.update({
    "font.family": ["Inter", "DejaVu Sans"], "font.size": 11,
    "svg.fonttype": "path", "figure.facecolor": SUP, "axes.facecolor": SUP,
})


def lienzo(w, h, xlim, ylim):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def guardar(fig, nombre):
    fig.savefig(OUT / nombre, format="svg", bbox_inches="tight", pad_inches=0.15)
    if "--png" in sys.argv:
        pathlib.Path("/tmp/figpng").mkdir(exist_ok=True)
        fig.savefig(pathlib.Path("/tmp/figpng") / nombre.replace(".svg", ".png"), dpi=100, bbox_inches="tight")
    plt.close(fig); print("ok", nombre)


def caja(ax, x, y, w, h, texto, fc=CAJA, ec=CAJA2, tc=TINTA, fs=10, r=0.08, lw=1.2, peso="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw))
    if texto:
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=tc,
                linespacing=1.2, fontweight=peso)


def flecha(ax, a, b, color=TINTA2, rad=0.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=12, color=color, lw=1.3,
                                 connectionstyle=f"arc3,rad={rad}", shrinkA=2, shrinkB=2))


def pagina(ax, x, y, w, h, titulo):
    caja(ax, x, y, w, h, None, fc=SUP, ec=TINTA2, r=0.06)
    ax.add_patch(FancyBboxPatch((x, y + h - 0.35), w, 0.35, boxstyle="round,pad=0,rounding_size=0.06",
                                fc=CAJA, ec=TINTA2, lw=1.2))
    ax.text(x + 0.15, y + h - 0.175, titulo, ha="left", va="center", fontsize=9, color=TINTA2)
    for i in range(5):
        ax.plot([x + 0.2, x + w - 0.2 - (0.5 if i % 2 else 0)], [y + h - 0.7 - i * 0.32] * 2,
                color=GRIS, lw=3, solid_capstyle="round")





def c4_ae():
    fig, axs = plt.subplots(1, 2, figsize=(10, 3.4))
    for ax in axs: ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis("off"); ax.add_patch(FancyBboxPatch((0.1, 0.1), 15.8, 8.8, boxstyle="round,pad=0,rounding_size=0.2", fc=SUP, ec=TINTA2, lw=1.3))
    a, b = axs
    a.text(0.8, 7.8, "Resultados", fontsize=14, fontweight="bold", color=TINTA, va="center")
    for i, t in enumerate(["Se analizaron 1200 doctorandos", "Grupo con tutoría: 8 % de abandono", "Grupo sin tutoría: 15 % de abandono", "Diferencia significativa (p < 0,01)", "Implicaciones para los programas"]):
        a.text(1.0, 6.4 - i * 1.15, "•  " + t, fontsize=10, color=TINTA, va="center")
    a.text(8, -0.6, "Título tema + viñetas", ha="center", fontsize=10, color=TINTA2)
    b.text(0.8, 7.9, "La tutoría redujo el abandono a la mitad", fontsize=12.5, fontweight="bold", color=TINTA, va="center")
    for x, v, t, c in ((4.5, 15, "Sin tutoría", "#a3a29e"), (10, 8, "Con tutoría", S[0])):
        b.add_patch(FancyBboxPatch((x, 1.2), 3.0, v * 0.36, boxstyle="round,pad=0,rounding_size=0.1", fc=c, ec="none"))
        b.text(x + 1.5, 1.2 + v * 0.36 + 0.3, f"{v} %", ha="center", fontsize=12, fontweight="bold", color=TINTA)
        b.text(x + 1.5, 0.6, t, ha="center", fontsize=10, color=TINTA)
    b.text(8, -0.6, "Afirmación + evidencia visual", ha="center", fontsize=10, color=TINTA2)
    guardar(fig, "c4_ae.svg")


if __name__ == "__main__":
    c4_ae()
