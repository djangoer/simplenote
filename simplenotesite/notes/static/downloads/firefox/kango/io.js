kango.IO=function(){this._rootName=kango.getExtensionInfo().package_id;this.init()};
kango.IO.prototype=kango.oop.extend(kango.IOBase,{_rootName:null,_registerResourceProtocol:function(){var a=Services.io.getProtocolHandler("resource").QueryInterface(Ci.nsIResProtocolHandler),b=Services.io.newFileURI(kango.__installPath);kango.__installPath.isDirectory()||(b=Services.io.newURI("jar:"+b.spec+"!/",null,null));a.setSubstitution(this._rootName,b)},_unregisterResourceProtocol:function(){Services.io.getProtocolHandler("resource").QueryInterface(Ci.nsIResProtocolHandler).setSubstitution(this._rootName,null)},
init:function(){this._registerResourceProtocol()},dispose:function(){this._unregisterResourceProtocol()},getExtensionFileUrl:function(a){return"chrome://"+this._rootName+"/content/"+a},getResourceUrl:function(a){return"resource://"+this._rootName+"/"+a}});kango.registerModule(kango.getDefaultModuleRegistrar("io",kango.IO));
