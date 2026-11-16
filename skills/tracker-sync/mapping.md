# Workflow artifacts in each tracker

| Artifact | GitHub Issues | YouTrack | Basecamp |
| -------- | ------------- | -------- | -------- |
| Pitch (shaped work) | Issue labelled `pitch` | Knowledge-base article (`create_article`), linked from a `Pitch` issue or tag | Message on the message board, or a Doc |
| Bet for a cycle | Milestone named for the cycle | Tag `bet-<cycle>` on the pitch issue, or an agile board sprint if the team uses one | A project (or to-do list group) for the bet |
| Scope | Sub-issue of the bet | Issue linked "subtask of" the bet (`link_issues`) | A to-do list per scope |
| Task inside a scope | Checklist line | Subtask, or a checklist in the description | A to-do in the scope's list |
| Bug report | Issue labelled `bug` | Issue of type Bug | A card in the Card Table (or the team's bug list) |
| Evidence, review result, "Verified on" | Comment | Comment (`add_issue_comment`) | Comment on the to-do or card |
| Hill chart | Comment with the SVG/PNG | Comment with the image attached | Basecamp's own hill chart on the scope lists; dots set by the person doing the work |
| Time per stage | Not tracked (note it in the retro) | `log_work` | Not tracked (note it in the retro) |
| Commit link | `Refs #12` in the message | Issue ID in the message (`PRJ-123`), which YouTrack links when the project has a VCS integration | Paste the commit URL in a comment |
| Done | Closed by the merged PR | State set to Fixed/Done after merge | To-do checked or card moved to Done |

Notes:

- Shape Up keeps no backlog. Pitches that weren't bet on are left alone, not
  queued; if an idea matters it comes back.
- YouTrack tools: `search_issues`, `get_issue`, `get_issue_fields_schema`,
  `create_issue`, `create_draft_issue`, `update_issue`, `link_issues`,
  `add_issue_comment`, `get_issue_comments`, `manage_issue_tags`,
  `create_article`, `update_article`, `search_articles`, `log_work`. Limit the
  set with the endpoint's `readOnlyTools` or `toolSubsets` parameters for
  read-only jobs.
- Basecamp MCP tools are domain tools (`basecamp_todos`, `basecamp_cards`,
  `basecamp_messages`, `basecamp_files`, `basecamp_recordings`, …) that each
  take an `action` and `params`. Start read-only jobs with
  `basecamp mcp --read-only`, and narrow domains with `--domains`.
