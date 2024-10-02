// services/auth.js
import {
    GoogleAuthProvider,
    getAdditionalUserInfo,
    signInWithPopup,
  } from 'firebase/auth';
  import { auth } from '../firebase/config'; // Adjust the path if necessary
  
  const provider = new GoogleAuthProvider();
  
  export async function signInWithGoogle() {
    let result = null;
    let error = null;
    let isNewUser = false;
  
    try {
      const userCredential = await signInWithPopup(auth, provider);
      result = userCredential;
  
      const additionalInfo = getAdditionalUserInfo(userCredential);
      isNewUser = additionalInfo.isNewUser;
    } catch (e) {
      error = { code: e.code, message: e.message };
    }
    return { result, isNewUser, error };
  }
  