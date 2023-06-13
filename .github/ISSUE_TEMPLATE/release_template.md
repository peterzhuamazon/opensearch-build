---
name: Release
title: "[RELEASE] Release version {{ env.VERSION }}"
labels: untriaged, release, v{{ env.VERSION }}
---

## Release OpenSearch and OpenSearch Dashboards {{ env.VERSION }}

I noticed that a manifest was automatically created in [manifests/{{ env.VERSION }}](/opensearch-project/opensearch-build/tree/main/manifests/{{ env.VERSION }}). Please follow the following checklist to make a release.

<details><summary>How to use this issue</summary>
<p>

## This Release Issue

This issue captures the state of the OpenSearch release, its assignee is responsible for driving the release. Please contact them or @mention them on this issue for help. There are linked issues on components of the release where individual components can be tracked.  More details are included in the Maintainers [Release owner](https://github.com/opensearch-project/opensearch-build/blob/main/MAINTAINERS.md#release-owner) section.

## Release Steps

There are several steps to the release process, these steps are completed as the whole release and components that are behind present risk to the release.  The release owner completes the tasks in this ticket, whereas component owners resolve tasks on their ticket in their repositories.

Steps have completion dates for coordinating efforts between the components of a release; components can start as soon as they are ready far in advance of a future release.


### Plugin List

To aid in understanding the state of the release there is a table with status indicating each component state. This is updated based on the status of the component issues.

</p>
</details>

### Preparation - __REPLACE_RELEASE-minus-14-days__

- [ ] Assign Primary and secondary release managers to OpenSearch release
    <details><summary>How release managers are assigned to a release?</summary>
    <p>
  
  The primary release managers to a specific OpenSearch release will be assigned through volunteer model. The request for release managers will be posted in [OpenSearch public slack workspace](https://opensearch.slack.com/archives/C0561HRK961) (under releases channel) and selected on first come first served (FCFS) model. <br>**Note:** The release managers should be maintainer of at least one repository under OpenSearch GitHub organization.
  
  </p>
  </details>
- [ ] Declare a pencils down date (__REPLACE_RELEASE-minus-14-days__) for new features to be merged and freeze.
- [ ] Update the Campaigns section to include monitoring campaigns during this release. 
- [ ] Update this issue so all `__REPLACE_RELEASE-__` placeholders have actual dates.
- [ ] Document any new quality requirements or changes (as needed) in a comment and update it following the release process. 
- [ ] [Create a release issue in every component repo](https://github.com/opensearch-project/opensearch-plugins/blob/main/META.md#create-an-issue-in-all-plugin-repos) based on [component release issue template](https://github.com/opensearch-project/opensearch-build/blob/main/.github/ISSUE_TEMPLATE/component_release_template.md) and link back to this issue, update plugin section with these links.
- [ ] Ensure the label is created in each plugin repo for this new version, and the next minor release. [Create a version label](https://github.com/opensearch-project/opensearch-plugins/blob/main/META.md#create-or-update-labels-in-all-plugin-repos)
- [ ] Ensure that all release issues created above are assigned to a release manager in the component team.
- [ ] Finalize scope and feature set using [the Public Roadmap](https://github.com/orgs/opensearch-project/projects/1).
    <details><summary>How to get the list of participating plugins?</summary>
    <p>

  Please use the previous version [input manifest](https://github.com/opensearch-project/opensearch-build/tree/main/manifests) to create the input manifest for the upcoming version. Post the plugin list on the manifest in [OpenSearch public slack workspace](https://opensearch.slack.com/archives/C0561HRK961) to get the feedback from component release managers. The component release managers are responsible for providing any new plugins, updating plugin list corresponding to a release to primary release manager.

  </p>
  </details>


- [ ] Increase the build frequency for the this release from once a day (H 1 * * *) to once every hour (H/60 * * * *) in [check-for-build jenkinsFile](https://github.com/opensearch-project/opensearch-build/blob/main/jenkins/check-for-build.jenkinsfile).
- [ ] Verify the above auto-build is correctly triggered every hour for the corresponding release version.
- [ ] Contact [opensearch-build repository maintainers](https://github.com/opensearch-project/opensearch-build/blob/main/MAINTAINERS.md) with any questions.

### Release Branch - _Ends __REPLACE_RELEASE-minus-10-days__

- [ ] Plugin versions are auto-incremented to {{ env.VERSION }} version and receive version increment PRs in plugin repositories.
    <details><summary>How to automatically increase plugin versions and send PRs?</summary>
    <p>

  Please contact one of the [opensearch-build repository maintainers](https://github.com/opensearch-project/opensearch-build/blob/main/MAINTAINERS.md) to trigger [OpenSearch Plugin Increment Workflow](https://github.com/opensearch-project/opensearch-build/actions/workflows/os-increment-plugin-versions.yml) and [OpenSearch-Dashboards Plugin Increment Workflow](https://github.com/opensearch-project/opensearch-build/actions/workflows/osd-increment-plugin-versions.yml). These workflows will automatically create PRs to the corresponding plugin repositories. Please make sure all the plugins (See above: How to get the list of participating plugins?) are included in the workflow files of these GitHub Actions.

  </p>
  </details>
  

- [ ] Plugin teams / component release manager to merge the version increment PRs after successful CI checks.
- [ ] [OpenSearch](https://github.com/opensearch-project/OpenSearch/branches) and [OpenSearch-Dashboards](https://github.com/opensearch-project/OpenSearch-dashboards/branches) core components create release branch (`<MajorVersion>.<MinorVersion>`).
- [ ] All plugin repos participating in this release create release branch (`<MajorVersion>.<MinorVersion>`).
    <details><summary>How to ensure that the teams take action in timely manner?</summary>
    <p>

  The discussions around blockers, gaps will happen in [OpenSearch public slack workspace](https://opensearch.slack.com/archives/C0561HRK961). The primary release manager assigned to a release will tag the secondary release managers, repo managers to get the status update on any pending action item.

  </p>
  </details>
  
- [ ] Primary release manager will be in contact with all component release managers, to ensure that all the components have merged the version increment PRs, cut release branch, and aware of the upcoming new release.

### Build infrastructure readiness - _Ends __REPLACE_RELEASE-minus-9-days__
- [ ] Create PRs to add all participating component / plugin to [manifests/{{ env.VERSION }}/opensearch-{{ env.VERSION }}.yml](/opensearch-project/opensearch-build/tree/main/manifests/{{ env.VERSION }}/opensearch-{{ env.VERSION }}.yml) and [manifests/{{ env.VERSION }}/opensearch-dashboards-{{ env.VERSION }}.yml](/opensearch-project/opensearch-build/tree/main/manifests/{{ env.VERSION }}/opensearch-dashboards-{{ env.VERSION }}.yml) with the corresponding checks.
- [ ] Monitor [distribution-build-opensearch](https://build.ci.opensearch.org/job/distribution-build-opensearch/) and [distribution-build-opensearch-dashboards](https://build.ci.opensearch.org/job/distribution-build-opensearch-dashboards) Jenkins workflows, to ensure the above added plugins are built correctly.
- [ ] Contact component release manager(s) if any of the participating component showing errors in above workflow runs.

### Code Complete - _Ends __REPLACE_RELEASE-minus-7-days___
- [ ] Make sure that the code for this specific version of the release is ready and the branch corresponding to this release has been updated in the release specific build manifest.
- [ ] Sync up with component release manager of each plugin, to gather current status, and inform everyone about the upcoming code complete and freeze date.
- [ ] Verify pull requests to add each component to [manifests/{{ env.VERSION }}/opensearch-{{ env.VERSION }}.yml](/opensearch-project/opensearch-build/tree/main/manifests/{{ env.VERSION }}/opensearch-{{ env.VERSION }}.yml) and [manifests/{{ env.VERSION }}/opensearch-dashboards-{{ env.VERSION }}.yml](/opensearch-project/opensearch-build/tree/main/manifests/{{ env.VERSION }}/opensearch-dashboards-{{ env.VERSION }}.yml) have been merged.
- [ ] Use Jenkins [release-notes-tracker](https://build.ci.opensearch.org/job/release-notes-tracker/) workflow to verify that all the components have updated their release notes in the corresponding `<MajorVersion>.<MinorVersion>` branch.
- [ ] Use this [release-notes generation tool](https://github.com/opensearch-project/opensearch-build/tree/main/scripts/release-notes) to generate consolidated release notes of all participating components to a rough draft, and create a PR in opensearch-build repository.
- [ ] Sync up with Tech Writers and product managers on the potential highlights of the release, update release-notes PR.

### Release testing - _Ends __REPLACE_RELEASE-minus-6-days___
- [ ] Run distribution build of both OpenSearch and OpenSearch-Dashboards Jenkins workflow by specifying `build_docker_with_build_number_tag` option.
- [ ] Declare and broadcast release candidate build along with instructions for performing sanity tests 

  <details><summary>How to broadcast release candidate?</summary>
    <p>
  
  Broadcast the release candidate in [OpenSearch public slack workspace](https://opensearch.slack.com/archives/C0561HRK961) and the release GitHub issue using below format to gather votes.

  ##### Please vote for release candidate 1 for OpenSearch <version>

  ######  The artifacts can be downloaded from:

  * OpenSearch - #Build-number (Note: Windows version does not have performance analyzer plugin)
    * arm64 [[manifest](manifest.yml)] [[tar](opensearch-vesion-linux-arm64.tar.gz)] [[rpm](opensearch-vesion-linux-arm64.rpm)][[deb](opensearch-version-linux-arm64.deb)]
    * x64 [[manifest](manifest.yml)] [[tar](opensearch-version-linux-x64.tar.gz)] [[rpm](opensearch-version-linux-x64.rpm)] [[deb](opensearch-version-linux-x64.deb)] [[windows](opensearch-version-windows-x64.zip)]
  * OpenSearch Dashboards - #Build-number
    * arm64 [[manifest](manifest.yml)] [[tar](opensearch-dashboards-vesion-linux-arm64.tar.gz)] [[rpm](opensearch-dashboards-vesion-linux-arm64.rpm)][[deb](opensearch-dashboards-version-linux-arm64.deb)]
    * x64 [[manifest](manifest.yml)] [[tar](opensearch-dashboards-version-linux-x64.tar.gz)] [[rpm](opensearch-dashboards-version-linux-x64.rpm)] [[deb](opensearch-dashboards-version-linux-x64.deb)] [[windows](opensearch-dashboards-version-windows-x64.zip)]

   ###### You can execute the tests directly using the below command:

    Testing the Distribution
      Tests the OpenSearch distribution, including integration, backwards-compatibility and performance tests. <br>

    `./test.sh <test-type> <test-manifest-path> <path>`

  More info on testing the distribution: https://github.com/opensearch-project/opensearch-build/blob/main/README.md#testing-the-distribution
        
   ###### You can also execute the tests in Jenkins (more in the following next steps):
     https://build.ci.opensearch.org/job/integ-test/
     https://build.ci.opensearch.org/job/integ-test-opensearch-dashboards/


  The vote will be open until next <PLACEHOLDER FOR DAY>, i.e. until [<PLACEHOLDER FOR DATE AND TIME>]

  [ ] +1 approve
  [ ] +0 no opinion
  [ ] -1 disapprove (and reason why)

  </p>
  </details>

- [ ] Stop builds for this version of OpenSearch and/or OpenSearch Dashboards in order to avoid accidental commits by updating OpenSearch [Jenkins file](https://github.com/opensearch-project/opensearch-build/blob/main/jenkins/opensearch/distribution-build.jenkinsfile) and OpenSearch dashboards [Jenkins file](https://github.com/opensearch-project/opensearch-build/blob/main/jenkins/opensearch-dashboards/distribution-build.jenkinsfile) by removing the previously scheduled runs in [check-for-build jenkinsFile](https://github.com/opensearch-project/opensearch-build/blob/main/jenkins/check-for-build.jenkinsfile) and send a PR. 
- [ ] Raise PR to lock input manifest refs of both OS and OSD builds with specific commit ids from distribution manifest of the release candidate to lock the commits to the RC build.
- [ ] Allow the community to sanity test and report critical issues found during testing. **Note**: Teams test their plugins within the distribution, ensuring integration, backwards compatibility, and performance tests.
- [ ] PR test manifests commits from previous release, suggest taking examples from at least 2.8.0 version and later.
- [ ] Execute automated [integration](https://build.ci.opensearch.org/job/integ-test/), [BWC](https://build.ci.opensearch.org/job/bwc-test/) and [performance tests](https://build.ci.opensearch.org/job/perf-test/) for OpenSearch.
- [ ] Execute automated [integration](https://build.ci.opensearch.org/job/integ-test-opensearch-dashboards/) for OpenSearch dashboards.
- [ ] Publish all test results in the comments of this release issue.

### Finalize the release candidate
- [ ] Finalize the release candidate for specific release, confirming all the test results are either passing or manually sign-off by component release manager(s).
- [ ] Get the Go / No-Go votes from project management committee (PMC)

### Release - _Ends {__REPLACE_RELEASE-day}_
- [ ] Verify [all issues labeled `v{{ env.VERSION }}` in all projects](https://github.com/opensearch-project/project-meta#find-labeled-issues) have been resolved.
- [ ] Complete [documentation](https://github.com/opensearch-project/documentation-website) for this release.
- [ ] Publish the release artifacts to all supported distribution channels (i.e. S3, Docker, Yum etc..) using [distribution build artifacts promotion](https://build.ci.opensearch.org/job/distribution-promote-artifacts/), [distribution build repo promotion](https://build.ci.opensearch.org/job/distribution-promote-repos/), [Docker promotion workflow](https://build.ci.opensearch.org/job/docker-promotion/), [maven publishing](https://build.ci.opensearch.org/job/publish-to-maven/), cloudfront invalidation, with 2-PR process alongside opensearch-build repository maintainers.
- [ ] Validate the artifacts in OpenSearch.org [downloads page](https://opensearch.org/downloads)
- [ ] Author [blog post](https://github.com/opensearch-project/project-website) for this release.
- [ ] Author [documentation updates](https://github.com/opensearch-project/documentation-website) for this release.
- [ ] __REPLACE_RELEASE-day - Publish to social media and channels - release is launched!

### Post Release
- [ ] Create [release tags](https://github.com/opensearch-project/opensearch-build/blob/main/jenkins/release-tag/release-tag.jenkinsfile) for each component with this [Jenkins workflow](https://build.ci.opensearch.org/job/distribution-release-tag-creation/).
- [ ] Replace refs in [manifests/{{ env.VERSION }}](/opensearch-project/opensearch-build/tree/main/manifests/{{ env.VERSION }}) with tags (tags/<MajorVersion>.<MinorVersion>.<PatchVersion> for OpenSearch / OpenSearch-Dashboards / functionalTestDashboards, and tags/<MajorVersion>.<MinorVersion>.<PatchVersion>.0 for all other components).
- [ ] If this is a major or minor version release, stop building previous patch version.
- [ ] Increment version for Helm Charts [(sample PR)](https://github.com/opensearch-project/helm-charts/pull/246) for the `{{ env.VERSION }}` release.
- [ ] Increment version for Ansible Charts [(sample PR)](https://github.com/opensearch-project/ansible-playbook/pull/50) for the `{{ env.VERSION }}` release.
- [ ] Prepare [for next patch release](https://github.com/opensearch-project/opensearch-plugins/blob/main/META.md#increment-a-version-in-every-plugin) by incrementing patch versions for each component, similar to above steps in `Release Branch`.
- [ ] Update [this template](https://github.com/opensearch-project/opensearch-build/blob/main/.github/ISSUE_TEMPLATE/release_template.md) with any new or missed steps.
- [ ] Create an issue for a retrospective, solicit feedback, and publish a summary.

### Components
__Replace with links to all component tracking issues.__

| Component | On track | Release Notes |
| --------- | -------- | ----- |
| {COMPONENT_ISSUE_LINK} | {INDICATOR}} | {STATUS} |

<details><summary>Legend</summary>
<p>

| Symbol | Meaning |
| -------- | ---------- |
| :green_circle: | On track with overall release |
| :yellow_circle: | Missed last milestone |
| :red_circle: | Missed multiple milestones |

</p>
</details>

### Campaigns 
 <details><summary>How to tag OpenSearch campaigns to this section?</summary>
    <p>

* Filter all the issues tagged to "campaign" along with specific " OpenSearch version label" across all participating GitHub repos and add them to this section. 

   </p>

   </details>
