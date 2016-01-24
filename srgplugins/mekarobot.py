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
import time
import threading
from math import degrees

# ROS IMPORTS
import rospy
import roslib
from sensor_msgs.msg import JointState


class ROSConnector(threading.Thread):

    def __init__(self, _topic):
        threading.Thread.__init__(self)
        self.rlock = threading.RLock()
        rospy.init_node('srgmekaplugin', anonymous=True)
        self.topic = _topic
        self.run_toggle = True
        self.head_j0 = 0.0
        self.head_j1 = 0.0

    def get_head_state(self, ros_data):
        self.rlock.acquire()
        ros_data.position[0] = self.head_j0
        ros_data.position[1] = self.head_j1
        self.rlock.release()

    def get_head_state(self):
        self.rlock.acquire()
        return float(degrees(self.head_j0)), float(degrees(self.head_j1))
        self.rlock.release()

    def run(self):
        print ">>> Initializing MEKA-ROS HEAD Subscriber to: %s" % self.inscope.strip()
        head_subscriber = rospy.Subscriber(self.topic, JointState, self.get_head_state, queue_size=1)
        while self.run_toggle is True:
            time.sleep(0.05)
        head_subscriber.unregister()
        print ">>> Deactivating MEKA-ROS HEAD Subscriber to: %s" % self.inscope.strip()


# THIS CLASS NEEDS TO BE IMPLEMENTED BY EACH PLUGIN
# TODO: Implement proper inheritance!
class SRGRobotFeedback:

    def __init__(self):
        threading.Thread.__init__(self)
        self.rlock = threading.RLock()
        self.mw = ROSConnector("/meka_roscontrol/joint_states")
        self.mw.start()

    # THIS METHOD NEEDS TO BE IMPLEMENTED BY EACH PLUGIN
    # TODO: Implement proper inheritance!
    def get_current_head_state(self):
        self.mw.get_head_state()

    def stop_head_state_sub(self):
        self.mw.run_toggle = False