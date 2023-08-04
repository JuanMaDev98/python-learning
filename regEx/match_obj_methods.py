# The table below summarizes the methods that are available for a match object match:

#        Method	                         Returns
#     match.group()	              The specified captured group or groups from match
#     match.__getitem__()	      A captured group from match
#     match.groups()	          All the captured groups from match
#     match.groupdict()	          A dictionary of named captured groups from match
#     match.expand()	          The result of performing backreference substitutions from match
#     match.start()	              The starting index of match
#     match.end()	              The ending index of match
#     match.span()	              Both the starting and ending indices of match as a tuple