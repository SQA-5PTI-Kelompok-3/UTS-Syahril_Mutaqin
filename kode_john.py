{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNm6uhL74g2R3BJeav+bzii"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aey8wyml8P0E"
      },
      "outputs": [],
      "source": [
        "jam = 52\n",
        "tarif = 15000\n",
        "if jam > 40:\n",
        "    upah = 40 * tarif + (jam - 40) * tarif * 1.5\n",
        "else:\n",
        "    upah = jam * tarif\n",
        "pengeluaran = 600000\n",
        "if upah > pengeluaran:\n",
        "    print(\"bisa menabung\")\n",
        "    print(\"tabungan:\", upah - pengeluaran)\n",
        "if upah == pengeluaran:\n",
        "    print(\"tidak bisa menabung\")\n",
        "else:\n",
        "    print(\"cari tambahan\")"
      ]
    }
  ]
}