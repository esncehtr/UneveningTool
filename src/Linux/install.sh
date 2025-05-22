#!/bin/bash

set -e

echo -e "\033[1;36m=== Установка UneveningTool ===\033[0m"

if [ -f /etc/arch-release ]; then
    DISTRO="arch"
    PKG="pacman"
elif [ -f /etc/debian_version ]; then
    DISTRO="debian"
    PKG="apt"
else
    echo -e "\033[1;31mНеподдерживаемый дистрибутив.\033[0m"
    exit 1
fi

echo -e "\033[1;33mОбновление системы...\033[0m"
if [ "$DISTRO" = "arch" ]; then
    sudo pacman -Syu --noconfirm
else
    sudo apt update && sudo apt upgrade -y
fi

echo -e "\033[1;33mУстановка необходимого..033[0m"
if [ "$DISTRO" = "arch" ]; then
    sudo pacman -S --noconfirm python python-pip android-tools python-colorama
else
    sudo apt install -y python3 python3-pip android-tools-adb android-tools-fastboot python3-colorama
fi

echo -e "\033[1;36m=== Проверка ===\033[0m"
python3 --version || echo -e "\033[1;31mPython не установлен.\033[0m"
pip3 --version || echo -e "\033[1;31mpip не установлен.\033[0m"
adb --version || echo -e "\033[1;31mADB не установлен.\033[0m"
fastboot --version || echo -e "\033[1;31mFastboot не установлен.\033[0m"

echo -e "\033[1;32mГотово!\033[0m"
