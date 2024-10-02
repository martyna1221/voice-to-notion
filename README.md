###

VIRTUAL ENVIRONMENT

###

1st things 1st, create a virtual environment & activate it

Create the `venv` in the outer most layer of the repository

On windows the commands are:
1. `python -m venv venv`
2. `.\venv\Scripts\activate`

This set up is a little bit unorthodox because it uses both NextJS and Python. The NextJS sign-in app
is located in the aptly named folder `nextjs-signin` & the Python is located in the `streamlit-app` folder

After you activate your `venv` from the root directory cd into the `streamlit-app` folder and run this command:

`pip install -r requirements.txt`

We've added our most used libraries to that file. If you use any others, add them to `requirements.txt` & rerun the
above command to add those dependencies to your `venv`


###

Why Streamlit?

###

We use Streamlit because it is a quick way to develop protoypes and MVPs in Python. It renders a frontend app without needing a
frontend developer. Additionally, it requires not dev-ops. This saves us alot of time

Streamlit is easy to use and there are alot of things that you can do!

Check our their docs: https://docs.streamlit.io/

###

The Setup

###

1. Copy service account JSON into `key.json` -> this is your way of accessing Firebase when running the app locally
2. If you need to add more tabs to the sidebar, place them inside of the `pages` folder. The tab name is the name of the .py file
3. If you need to add any functions add them to the `applications` folder (Jacob has set up a connection to Firebase in the `database,py` file)
4. Add your API keys and whatnot into the `.env` file

###

Running Streamlit

###

To run the app type in this command into the terminal: `streamlit run main.py`

Make sure you are inside the `streamlit-app` folder. If you're not, please reference it accordingly

You should see the app run on this URL: `http://localhost:8501/`

Once you start creating changes, you can see updates by clicking on either `Rerun` or `Always rerun` in the upper righthand corner

###

NextJS Sign-In App Setup

###

1. Ask one of the MJV team members for the Firebase config for the specific project that you're working on

It looks something like this:

const firebaseConfig = {
  apiKey: 'xxx',
  authDomain: 'xxx',
  projectId: 'xxx',
  storageBucket: 'xxx',
  messagingSenderId: 'xxx',
  appId: 'xxx',
  measurementId: 'xxx'
};

Without this constant, SSO will not work

You will input this into the `firebase/config.js` file

In the same file you'll also need to update line `router.push('xxx');`

Change this to the URL you get from pushing the `streamlit-app` to GCP (more on this later)

If a project only requires you to have Google SSO or a combination of Linkedin & username + password login, you can comment out/delete the irrelevant sections

Add static images in the `public` folder; this is where our SSO pngs are stored

To run this app, `cd` into the `nextjs-singin` folder and run these 2 commands:
1. `npm install`
2. `npm run dev`

Note: If you've never run `npm` on your computer you'll have to download it

### 

Testing

###

1. Run the `nextjs-sigin` on one terminal -> `localhost:3000/signin`

2. Run the `streamlit-app` on another terminal -> `localhost:8501`

3. Replace the `router.push('xxx');` line (in the `firebase/config.js` file) to `localhost:8501` - you can now route to the streamlit app from the signin page (09/02/24 - The backend team is working on creating a nice workaround here with .env variables)

4. If you get a firebase error, you'll have to add `localhost:3000` to Authorized Domains within the Firebase console (if that hasn't already been configured for project; it's the same process for when you push to GCP) - contact either Martyna or Jacob if you can't figure it out

4. Now you can test your code! Whenever you make a change in streamlit you can click on the `Rerun` or `Always rerun` buttons in the upper right hand corner; this alows the code to recompile without you having to build via the terminal over and over again

Because of the implements `login()` function, even if a user guesses the streamlit URL, it forces them to first login before accessing the app itself; this means that even if you go to `localhost:8501` it'll reroute you to `localhost:3000/signin`


###

Pushing to GCP

###

1. In the cloudbuild.yaml file replace all instance of `<PROJECT-ID>` with the GCP project you are working on; if you don't know the ID
of the project you're working on please let someone know and we'll get it for you

2. Hop on a call with either Martyna or Jacob & we'll go through GCP CI/CD configuration steps

3. Remember you'll have to change this line `router.push('xxx');` to the URL given by GCP (09/02/24 - The backend team is working on creating a nice workaround here with .env variables)

Happy coding! MJV 2024