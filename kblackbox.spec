Name:		kblackbox
Version:	15.08.3
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
%doc %{_docdir}/HTML/*/kblackbox
%{_bindir}/kblackbox
%{_datadir}/appdata/kblackbox.appdata.xml
%{_datadir}/applications/org.kde.kblackbox.desktop
%{_iconsdir}/hicolor/*/apps/kblackbox.png
%{_datadir}/kblackbox
%{_datadir}/kxmlgui5/kblackbox/kblackboxui.rc

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
