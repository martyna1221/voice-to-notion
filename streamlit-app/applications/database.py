from applications import db
from google.cloud import firestore

def create_firestore_document(collection_name, data):
    """
    Create a document in the 'collection_name' collection.
    Returns the document ID of the created document.
    """
    doc_ref = db.collection(collection_name).document()
    doc_ref.set(data)
    return doc_ref.id

def update_firestore_document(collection_name, document_id, data):
    """
    Update an existing document in the 'collection_name' collection.
    Prints a success message upon successful update.
    """
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.update(data)
    print(f'Document with ID: {document_id} in collection: {collection_name} updated successfully.')

def create_user(email):
    """
    Create a new user document in the 'users' collection.
    """
    user_ref = db.collection('users').document(email)
    user_ref.set({
        'email': email,
        'created': firestore.SERVER_TIMESTAMP
    })

def get_user(email):
    """
    Get the user document from the 'users' collection.
    """
    user_ref = db.collection('users').document(email)
    return user_ref.get().to_dict()
