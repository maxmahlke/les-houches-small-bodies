<p align="center">
  <img width="260" src="https://raw.githubusercontent.com/maxmahlke/les-houches-small-bodies/main/00-Resources/logo.svg">
  </br>
  <h1 align="center">Les Houches Index of Small-Body Tools</h1>
</p>


<p align="center">
  <a href="https://github.com/maxmahlke/les-houches-small-bodies#databases"> Databases </a> - <a href="https://github.com/maxmahlke/small-bodes-les-houches#webservices"> Webservices </a> - <a href="https://github.com/maxmahlke/small-bodes-les-houches#software"> Software </a>
</p>

# Databases

Where to get data.

## AstDyS <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://newton.spacedys.com/astdys/
- Dynamical properties, osculating and proper elements, dynamical families.

## Asteroid Families Portal <img src="https://img.shields.io/badge/Asteroids-red"/>

- http://asteroids.matf.bg.ac.rs/fam/properelements.php
- Catalogs of proper elements and dynamical family membership

## Centre de Données de Strasbourg (CDS) <img src="https://img.shields.io/badge/Asteroids-red"/><img src="https://img.shields.io/badge/Comets-blue"/><img src="https://img.shields.io/badge/Meteorites-purple"/>

- http://cdsweb.u-strasbg.fr/
- Many catalogs from publications. However, the CDS is not built for moving objects.

## DAMIT <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://astro.troja.mff.cuni.cz/projects/damit/
- 3D shape models of asteroids from light curve inversion tehcniques

## IMCCE SsODNet  <img src="https://img.shields.io/badge/Asteroids-red"/>

- Form: https://ssp.imcce.fr/forms/ssocard
- API: https://ssp.imcce.fr/webservices/ssodnet/

Huge compilation of data from other resources listed here and published literature, view several levels of access:
- `quaero`: All names and aliases
- `datacloud`: Bulk access to data
- `ssocard`: Best properties for a given SSO
- `ssobft`: All best properties for all SSOs at once

## JPL SBDB <img src="https://img.shields.io/badge/Asteroids-red"/><img src="https://img.shields.io/badge/Comets-blue"/>

- Form: https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html
- API: https://ssd.jpl.nasa.gov/api.html

Compilation of parameters from many sources.

## Lowell Observatory <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://asteroid.lowell.edu/
- The ASTORB catalog of osculating elements and compilation of properties.

## M4AST <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://spectre.imcce.fr/m4ast/
- A compilation of visible and near-infrared spectra of asteroids, with tools for analysis

## Minor Planet Center (MPC) <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- https://minorplanetcenter.net/
- Central point for astrometric observations, observatory codes, orbits.

## NEODyS <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://newton.spacedys.com/neodys/
- Similar to AstDyS, for NEAs

## OCA MP3C <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://mp3c.oca.eu/
- Compilation of data from both large repositories and literature.

## PDS Small Body Node (PDS SBN) <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- https://sbn.psi.edu/pds/
- Many standardized catalogs (well-documented PDS format) on SSOs, from space missions, observing campaigns and surveys, and derived properties.

## SSHADE <img src="https://img.shields.io/badge/Meteorites-purple"/>

- https://www.sshade.eu/
- Collections of spectra acquired in laboratory (meteorites, ices, minerals)

## SiMDA <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://astro.kretlow.de/?SiMDA
- Compilation of masses, diameters, and density of asteroids

# Webservices

Where to process data online.

## classy <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://classy.streamlit.app/
- Web interface of the [`classy`](https://github.com/maxmahlke/les-houches-small-bodies#classy--1) `python`, offering access to the spectra database and the classification of public spectra and of your own observations

## IMCCE VOSSP <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- Forms: https://ssp.imcce.fr/forms
- APIs: https://ssp.imcce.fr/webservices/
- Several services for SSOs:
  - `SkyBot`: cone-search to list SSOs in a field of view
  - `SkyBot 3D`: get the position of all SSOs at a given epoch
  - `Miriade/ephemcc`: compute the ephemerides of positions, orientations, rise-transit-set, *etc*)
  - `Miriade/ephemph`: compute the phyiscal ephemerides (orientations)
  - `Miriade/rts`: compute the rise-transit-set times
  - `Miriade/vision`: tool to plan nights of observations


## JPL Solar System Dynamics <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- Forms: https://ssd.jpl.nasa.gov/
- APIs: https://ssd-api.jpl.nasa.gov/
- Several services for SSOs:
  - `Horizons`: Compute ephemerides
  - `Identification`: List SSOs in a field of view
  - `What's Observable?`: List all SSOs visible from a location


## Lowell Observatory services <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- https://asteroid.lowell.edu/
- Several services for SSOs:
  - `AstInfo`: simple access to the main information from PDS for a single object
  - `AstObs`: observing conditions for a list of targets in a given observatory
  - `AstFinder`: to build finding charts
  - `AstEph`: compute the ephemerides of position
  - `Comet Fluorescence Efficiencies`: Comet fluorescence efficiencies and Haser model


## M4AST <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://spectre.imcce.fr/m4ast/
- Tools for taxonomy classification and band analysis of spectra

## Meteoritical Bulletin <img src="https://img.shields.io/badge/Meteorites-purple"/>

- https://www.lpi.usra.edu/meteor/
- *The* database of meteorites: Official names, classifications, fall/find statistics

## Minor Planet Center <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- https://minorplanetcenter.net/
- **The** official place to send/get astrometry of SSO.

## NASA Antarctic Meteorites <img src="https://img.shields.io/badge/Meteorites-purple"/>

- https://www-curator.jsc.nasa.gov/antmet/
- Like the meteoritical bulletin + it has an API! But it's only for Antarctic meteorites.

## SVO Filter Profile Service <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- http://svo2.cab.inta-csic.es/theory/fps/
- A huge compilation of information on filters: Zero Point, transmission curve, etc...

## VESPA <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>
- http://vespa.obspm.fr/planetary/data/
- Hub allowing to query many different services with a TAP interface

# Software

How to process data locally.

## ATM <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://github.com/moeyensj/atm
- A `python` package to build asteroid thermal models

## astroquery <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- https://astroquery.readthedocs.io/en/latest/
- A `python` package offering access to various astronomical databases via a unified interface

## classy <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://github.com/maxmahlke/classy
- A `python` package for easy access and analysis to (almost) all asteroid spectra out there and
taxonomic classification in multiple systems

## NEATM <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://github.com/MigoMueller/NEATM
- A `python` implementation of the Near-Earth Asteroid Thermal Model (NEATM)

## OpenOrb <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- https://github.com/oorb/oorb
- Open-source orbit computation written in Fortran

## Photometry Pipeline <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- https://photometrypipeline.readthedocs.io/en/latest/
- A versatile and user-friendly python package for measuring SSO photometry in images

## pyedra <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://github.com/milicolazo/Pyedra
- A `python` package for phase-function fitting using different photometric models

## rocks <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://github.com/maxmahlke/rocks
- A `python` package offering simple access to all data and services of [SsODNet](https://github.com/maxmahlke/les-houches-small-bodies#imcce-ssodnet--):
best estimates of dynamical and physical parameters of asteroids, compilation
of literature values, and name resolver.

## sbpy <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/></br>

- https://sbpy.readthedocs.io/en/latest/index.html
- `astropy`-affiliated `python` package with functions for planetary astronomy:
data access, photometric and spectrophotometric analysis, and more.
Planetary astronomy functions
