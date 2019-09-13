# Recap Time Probot App Docs: Stale Support Tickets (aka Stale Issues & Pull Requests)

When an issue or pull request doesn't had recent activity for up to 60 days, our Recap Time Probot app will
fire up an automated message before it will automatically close after another 14 days.

# How this

## The Configuration Code

You can also see this code on `.github/stale.yml` folder on GitHub.

    # Number of days of inactivity before an issue becomes stale
    daysUntilStale: 60
    # Number of days of inactivity before a stale issue is closed
    daysUntilClose: 14
    # Issues with these labels will never be considered stale
    exemptLabels:
      - pinned
      - security
      - dependencies
    # Label to use when marking an issue as stale
    staleLabel: stale, inactive-support-ticket
    # Comment to post when marking an issue as stale. Set to `false` to disable
    markComment: >
      To whom reading this note,
    
      This issue has been **automatically marked** as stale because it has not had
      recent activity. It will be closed if no further activity occurs. To learn more
      about our policies regarding issues marked as stale by 
      [Recap Time Probot App](https://github.com/marketplace/recap-time-probot-app),
      our in-house GitHub bot deployment, see `docs/recap-time-probot-app/stale.md`
      file for more info.
    # Comment to post when closing a stale issue. Set to `false` to disable
    closeComment: false