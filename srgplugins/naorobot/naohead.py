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

# STD IMPORTS
import sys
import time
import threading
from math import degrees

# NAOQi
from naoqi import ALProxy


class QiConnector(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.rlock = threading.RLock()
        try:
            self.motionProxy = ALProxy("ALMotion", "129.70.143.36", 9559)
        except Exception, e:
            print "ERROR >>> Could not create proxy to ALMotion"
            print e
            sys.exit(1)
        self.run_toggle = True
        self.head_pitch = 0.0
        self.head_yaw   = 0.0

    def get_head_state_qi(self):
        self.head_pitch = self.motionProxy.getAngles("HeadPitch", True)
        self.head_yaw = self.motionProxy.getAngles("HeadYaw", True)

    def get_head_state(self):
        return float(degrees(self.head_pitch[0])), float(degrees(self.head_yaw[0]))

    def run(self):
        print ">>> Initializing NAOQI HEAD Subscriber"
        while self.run_toggle is True:
            time.sleep(0.05)
            self.get_head_state_qi()
        print ">>> Deactivating NAOQI HEAD Subscriber"


# THIS CLASS NEEDS TO BE IMPLEMENTED BY EACH PLUGIN
# TODO: Implement proper inheritance!
class SRGNaoRobotFeedback:

    def __init__(self):
        self.mw = QiConnector()
        self.mw.start()

    # THIS METHOD NEEDS TO BE IMPLEMENTED BY EACH PLUGIN
    # TODO: Implement proper inheritance!
    def get_current_head_state(self):
        return self.mw.get_head_state()

    # THIS METHOD NEEDS TO BE IMPLEMENTED BY EACH PLUGIN
    # TODO: Implement proper inheritance!
    def stop(self):
        self.mw.run_toggle = False
