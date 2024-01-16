#!/usr/bin/env python3

from astroquery.mpc import MPC
result = MPC.query_object('asteroid', number=56788)
print(result[0]['name'], result[0]['tisserand_jupiter'])


