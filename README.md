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

## Centre de Données de Strasbourg (CDS) <img src="https://img.shields.io/badge/Asteroids-red"/><img src="https://img.shields.io/badge/Comets-blue"/><img src="https://img.shields.io/badge/Meteorites-orange"/>

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

- https://asteroid.lowell.edu/main/
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

## SSHADE <img src="https://img.shields.io/badge/Meteorites-orange"/>

- https://www.sshade.eu/
- Collections of spectra acquired in laboratory (meteorites, ices, minerals)

## SiMDA <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://astro.kretlow.de/?SiMDA
- Compilation of masses, diameters, and density of asteroids

## VESPA <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>
- http://vespa.obspm.fr/planetary/data/
- Hub allowing to query many different services with a TAP interface

# Webservices

Where to process data online.

## classy <img src="https://img.shields.io/badge/Asteroids-red"/>

Taxonomic classification and spectra aggregator

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
  - `What's Observable?`: Lsit all SSOs visible from a location


## Lowell Observatory services <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://asteroid.lowell.edu/
- Several services for SSOs:
  - `AstInfo`: simple access to the main information from PDS for a single object
  - `AstObs`: observing conditions for a list of targets in a given observatory
  - `AstFinder`: to build finding charts
  - `AstEph`: compute the ephemerides of position


## M4AST <img src="https://img.shields.io/badge/Asteroids-red"/>

- https://spectre.imcce.fr/m4ast/
- Tools for taxonomy classification and band analysis of spectra


## Minor Planet Center <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- https://minorplanetcenter.net/
- **The** official place to send/get astrometry of SSO.

## OpenOrb

- https://github.com/oorb/oorb
- Open-source orbit computation

## SVO Filter Profile Service <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- http://svo2.cab.inta-csic.es/theory/fps/
- A huge compilation of information on filters: Zero Point, transmission curve, etc...

# Software

How to process data locally.

## astroquery <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

Access to various databases via a unified interface

## classy <img src="https://img.shields.io/badge/Asteroids-red"/>

Taxonomic classification and spectra aggregator

## Photometry Pipeline <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/>

- https://photometrypipeline.readthedocs.io/en/latest/
- A versatile and user-friendly python package for measuing SSO photometry in images

## pyedra <img src="https://img.shields.io/badge/Asteroids-red"/>

Phase-function fitting

## rocks <img src="https://img.shields.io/badge/Asteroids-red"/>

Access to all data on SsODNet

## sbpy <img src="https://img.shields.io/badge/Asteroids-red"/> <img src="https://img.shields.io/badge/Comets-blue"/></br>

Planetary astronomy functions
