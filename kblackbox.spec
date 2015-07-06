Name:		kblackbox
Version:	15.04.3
Release:	1
Epoch:		1
Summary:	Find atoms in a grid by shooting electrons
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kblackbox
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)

%description
KBlackbox is a game of hide and seek played on a grid of boxes where the
computer has hidden several balls. The position of the hidden balls can be
deduced by shooting beams into the box.

%files
%{_kde_bindir}/kblackbox
%{_kde_applicationsdir}/kblackbox.desktop
%{_kde_appsdir}/kblackbox
%{_kde_docdir}/*/*/kblackbox
%{_kde_iconsdir}/hicolor/*/apps/kblackbox.png

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
