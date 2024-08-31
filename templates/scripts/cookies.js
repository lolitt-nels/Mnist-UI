function getCookie(key){	      
    for(var _ of document.cookie.split(";")){
          _ = _.split("=")	
      if(_[0] == key){
        return decodeURIComponent(_[1])
      }    
    }  
    return null;
  }