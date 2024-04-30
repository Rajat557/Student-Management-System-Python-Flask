from main import app
import adminlogin as ad
import addstudnt as asd
import addattend as add
import search as sh
import section as st
import editstud as et
import userEdit as ut
import deletestud as ds
import generalinfo as gni
import userform as uf
import marks as ms
import fifth as sx
import sixth as ff
import seventh as sev
import eighth as eg 
import nineth as nin
import tenth as tt
import useresult as rs
import fifthres as fr
#---------------url for adminLogin---------------------
app.add_url_rule("/",view_func=ad.login,methods=["GET","POST"])
app.add_url_rule("/userLogin",view_func=ad.login1,methods=["GET","POST"])
app.add_url_rule("/register",view_func=ad.register,methods=["GET","POST"])
app.add_url_rule("/adminHome",view_func=ad.adminHome)
app.add_url_rule("/userHome",view_func=ad.userHome)
app.add_url_rule("/Logout",view_func=ad.Logout)

#-----------------url for adding students---------------------#
app.add_url_rule("/addStud",view_func=asd.addStud,methods=["GET","POST"])

#----------------url for adding attendance----------------------#
app.add_url_rule("/addattend",view_func=add.addAttend,methods=["GET","POST"])

#-----------------url for search---------------#
app.add_url_rule("/search",view_func=sh.search,methods=["GET","POST"])

#-----------------url for section---------------#
app.add_url_rule("/section",view_func=st.section,methods=["GET","POST"])

#------------------url for edit/delete-------------#
app.add_url_rule("/editStudent/<id>",view_func=et.editStudent,methods=["GET","POST"])
app.add_url_rule("/deleteStudent/<id>",view_func=ds.deleteStud,methods=["GET","POST"])
app.add_url_rule("/edit",view_func=ut.editStudent1,methods=["GET","POST"])

#-------------------url for profile----------------#
app.add_url_rule("/profile",view_func=ad.profile,methods=["GET","POST"])
app.add_url_rule("/adddetails",view_func=uf.addDet,methods=["GET","POST"])

#---------------------url for marks-------------------#
app.add_url_rule("/marks",view_func=ms.showstd,methods=["GET","POST"])
app.add_url_rule("/fifth",view_func=sx.fifth,methods=["GET","POST"])
app.add_url_rule("/sixth",view_func=ff.sixth,methods=["GET","POST"])
app.add_url_rule("/seventh",view_func=sev.seventh,methods=["GET","POST"])
app.add_url_rule("/eighth",view_func=eg.eighth,methods=["GET","POST"])
app.add_url_rule("/nineth",view_func=nin.nineth,methods=["GET","POST"])
app.add_url_rule("/tenth",view_func=tt.tenth,methods=["GET","POST"])
app.add_url_rule("/result",view_func=rs.result,methods=["GET","POST"])