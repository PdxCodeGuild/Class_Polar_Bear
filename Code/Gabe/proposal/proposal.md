# Gabe's Proposal
** By Gabe Chacon **

## Name Ideas:
- The Markdown
- The Daily Developer
- Wake Up Developers
- The Snooze

<br>

## Project Overview
Like Medium.com, this site is for developers to express their opinions and all things code. Unlike medium.com , this will be strictly limited to coding. Framework will be Vue, backend will be Django. I will use Sass for CSS styling, axios for REST calling.

<br>

## Functionality
- User will be prompted to sign in or create an account.
- The user will be able to make own profile, and collect followers similar to YouTube and other social media.
- The user add personal photos to webpage to style their own page.
- The user can post articles and photos.
- The user will recieve likes and dislikes, and other users can subscribe to their channel.
- Users can comment on posts.
- Creators can block/unsubscribe other users.
- Home page will have top articles based on views and/or likes.
- Users can view any article and subscribe to any creator.
- Users can save posts.
- Users can search specific articles.
- Side pannel will contain subscriptions, saved articles, history, and recently liked posts

<br>

## Data Model
### User
- name
- email
- date_created
- logged_in (default false)

### Profile
- user_id (foreign key)
- banner_photo
- profile_photo
- description/bio

### Posts
- user_id (foreign key)
- title
- body
- photos
- category
- likes
- dislikes

### Comments
- post_id (foreign key)
- user_id (foreign key)
- body
- likes
- dislikes

### UserHistory
- user_id (foreign key)
- post_id (foreign key)

### Subscriptions
- creater_user_id (foreign key)
- subscribers_user_id (foreign key)

### SavedArticles
- user_id (foreign key)
- post_id (foreign key)

<br>

## Schedule
### Milestone 1
Create user profile, with basic post capabilities. Create Homepage to view everone's posts.

### Milestone 2
Create like, dislike, and comment capabilities

### Milestone 3
Create subscription capabilities

### Milestone 4
Make ranking algo
