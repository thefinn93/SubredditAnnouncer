###
# Copyright (c) 2012, Finn Herzfeld
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.conf as conf
import supybot.registry as registry
from supybot.i18n import PluginInternationalization

_ = PluginInternationalization('SubredditAnnouncer')


def configure(advanced):
    conf.registerPlugin('SubredditAnnouncer')

SubredditAnnouncer = conf.registerPlugin('SubredditAnnouncer')

checkinterval_description = "How often, in minutes, to check reddit for new posts"
conf.registerGlobalValue(SubredditAnnouncer, 'checkinterval',
                         registry.NonNegativeInteger(5, checkinterval_description))

domain_description = "The domain to check. Probably http://www.reddit.com unless you've got a "
domain_description += "different reddit install"

conf.registerGlobalValue(SubredditAnnouncer, 'domain',
                         registry.String("http://www.reddit.com", domain_description))

redditname_descripton = "The name of the reddit install. Not really a big deal. Leave blank to not "
redditname_descripton += "have the [reddit] part of the announce message"
conf.registerGlobalValue(SubredditAnnouncer, 'redditname',
                         registry.String("Reddit", redditname_descripton))

shortdomain_description = "The short domain to use. Probably http://redd.it unless you've got your "
shortdomain_description += " own reddit install. If you don't have a short domain just set it to "
shortdomain_description += "your long domain"
conf.registerGlobalValue(SubredditAnnouncer, 'shortdomain',
                         registry.String("http://redd.it", shortdomain_description))


configfile_description = "The configuration file used for setting up the subreddit/channels"
configfile_default = conf.supybot.directories.data.dirize("subredditAnnouncer.ini")
conf.registerGlobalValue(SubredditAnnouncer, 'configfile',
                         registry.String(configfile_default, configfile_description))
