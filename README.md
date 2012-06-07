# ColorBrewer for Python

This module contains the colors from [Cynthia Brewer][cab38]'s [ColorBrewer][cb] packaged
for easy import and reuse in Python.


## API

The API attempts to follow Color Brewer as closely as possible:

- All color systems are all available in the module namespace.
- Additionally, they are organized into three groups to be used depending on how you
  want to steer the viewer to interpret the data:
    - `sequential`: ordered, with contrast peaking on either end; further subdivided into
        `multihue` and `singlehue`.
    - `divergent`: ordered, with contrast peaking in the middle as well as either end.
    - `qualitative`: unordered, with contrast at every step, ideal for categorical data.
- The color systems offer their continuum broken into waypoints. All offer all breakdowns
  between 3 and 9 color points; the `divergent` systems usually have entries for 3 through 11.


### Color Groups

- sequential
    - multihue
        - YlGn
        - YlGnBu
        - GnBu
        - BuGn
        - PuBuGn
        - PuBu
        - BuPu
        - RdPu
        - PuRd
        - OrRd
        - YlOrRd
        - YlOrBr
    - singlehue
        - Purples
        - Blues
        - Greens
        - Oranges
        - Reds
        - Greys

- diverging
    - PuOr
    - BrBG
    - PRGn
    - PiYG
    - RdBu
    - RdGy
    - RdYlBu
    - Spectral
    - RdYlGn

- qualitative
    - Pastel1
    - Pastel2
    - Dark2
    - Accent
    - Paired
    - Set1
    - Set2
    - Set3


## Information

Copyright (c) 2002 Cynthia Brewer, Mark Harrower, and The Pennsylvania State University.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software distributed 
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR 
CONDITIONS OF ANY KIND, either express or implied. See the License for the 
specific language governing permissions and limitations under the License.

See the [ColorBrewer updates][copyright] for updates to copyright information.

---

Translation to Python by David Schoonover and released under the MIT license.


[cab38]: http://www.personal.psu.edu/cab38/ "Cynthia Brewer"
[cb]: http://colorbrewer.org/ "ColorBrewer"
[copyright]: http://www.personal.psu.edu/cab38/ColorBrewer/ColorBrewer_updates.html "ColorBrewer Copyright"
