// pages/signin.js
import Image from 'next/image';
import Link from 'next/link';
import { useState } from 'react';
import { signInWithGoogle } from '../services/auth';
import { useRouter } from 'next/router';

const Signin = () => {
  const [error, setError] = useState(null);
  const router = useRouter();

  const handleGoogleSignIn = async () => {
    try {
      const { result, isNewUser, error } = await signInWithGoogle();
      if (error) {
        setError(error.message);
      } else {
        // Handle successful sign-in
        console.log('Sign-in successful:', result);
        const email = result.user.email;
        if (isNewUser) {
          console.log('New user');
        } else {
          console.log('Existing user');
        }
        router.push(`http://localhost:8501/?email=${encodeURIComponent(email)}`); /* TODO: update URL */
      }
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="bg-black flex items-center justify-center h-screen">
      <div className="mx-auto">
        <div className="bg-gray-900 p-9 rounded-lg flex flex-col items-center">
          <div>
            <Image src="/Logo.png" alt="logo" width={110} height={35} />
          </div>
          <p className="text-red-600 mt-5 text-lg font-semibold">xxx</p>
          <p className="text-white mt-5 text-xl">Welcome Back</p>
          <div className="mt-6 flex flex-col items-center gap-8">
            <input
              className="w-full bg-transparent border border-white/10 rounded-md p-4 lg:pr-48 text-base text-white"
              type="text"
              placeholder="Enter email address"
            />
            <button className="w-full p-4 border border-white/10 rounded-md text-white bg-white/5">
              Continue
            </button>
            <p className="text-white">
              You have an account? <Link href="/signup">Sign Up</Link>
            </p>
            <div className="relative">
              <p className="text-white">OR</p>
              <span className="absolute block lg:w-44 w-20 h-px bg-gray-300 left-10 top-1/2 transform -translate-y-1/2"></span>
              <span className="absolute block lg:w-44 w-20 h-px bg-gray-300 right-10 top-1/2 transform -translate-y-1/2"></span>
            </div>
            <button onClick={handleGoogleSignIn}
              className="lg:w-104 p-4 border border-white/10 rounded-md text-white bg-transparent flex justify-center items-center gap-6">
              <Image src="/Google.png" width={20} height={20} alt="google" />
              Continue with Google
            </button>
          </div>
          {error && <p className="text-red-500 mt-4">{error}</p>}
        </div>
        <div className="flex gap-5 text-white items-center justify-center pt-4">
          <button className="relative pr-5">Terms of Use</button> |
          <button>Privacy Policy</button>
        </div>
      </div>
    </div>
  );
};

export default Signin;
