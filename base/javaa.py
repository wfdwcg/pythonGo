import jpype
from jpype import *

startJVM(getDefaultJVMPath(), "-ea")
java.lang.System.out.println("Hello World")
shutdownJVM()


# jvmPath = jpype.getDefaultJVMPath()
# ext_classpath = './koushao-server-1.0-SNAPSHOT.jar'
# jvmArg = '-Djava.class.path=' + ext_classpath
# if not jpype.isJVMStarted():
#     jpype.startJVM(jvmPath, jvmArg)
#     TA = jpype.JPackage('cn.net.koushao.server.util').LogUtil
#     jd = TA()
#     jd.printInfoLog("hhhhilo")
#     system = jpype.java.lang.System
#     system.out.println("call system method")
# jpype.shutdownJVM()