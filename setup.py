"""

Copyright(c) <Florian Lier, Simon Schulz>
http://opensource.cit-ec.de/fsmt

This file may be licensed under the terms of the
GNU Lesser General Public License Version 3 (the ``LGPL''),
or (at your option) any later version.

Software distributed under the License is distributed
on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
express or implied. See the LGPL for the specific language
governing rights and limitations.

You should have received a copy of the LGPL along with this
program. If not, go to http://www.gnu.org/licenses/lgpl.html
or write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

The development of this software was supported by the
Excellence Cluster EXC 277 Cognitive Interaction Technology.
The Excellence Cluster EXC 277 is a grant of the Deutsche
Forschungsgemeinschaft (DFG) in the context of the German
Excellence Initiative.

Authors: Florian Lier, Simon Schulz
<flier, sschulz>@techfak.uni-bielefeld.de

"""

from setuptools import setup, find_packages

version = "0.1"
filename = "0.1"

setup(name="simplerobotgazeplugins",
      version=filename,
      description="Plugins for the Simple Robot Gaze Software",
      long_description="These Plugins are implemented in order to allow for a closed loop interaction",
      author="Florian Lier, Simon Schulz",
      author_email="flier[at]techfak.uni-bielefeld.de and sschulz[at]techfak.uni-bielefeld.de",
      url="https://github.com/CentralLabFacilities/simple_robot_gaze_plugins.git",
      download_url="https://projects.cit-ec.uni-bielefeld.de/git/flobi.demo.git",
      packages=find_packages(exclude=["*.tests",
                                      "*.tests.*",
                                      "tests.*",
                                      "tests"]),
      keywords=['HLRC', 'Robot Gaze'],
      license="LGPLv3",
      classifiers=[
          'Development Status :: Beta',
          'Environment :: Console',
          'Environment :: Robotics',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or ' +
          'Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Markup :: XML'
      ],
)
