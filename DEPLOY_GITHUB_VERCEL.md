# GitHub + Vercel 发布与更新流程

适用项目：`/Users/lumine/Desktop/personal-website`

## 1) 一次性初始化（只做一次）

### 1.1 确认本地仓库
```bash
cd /Users/lumine/Desktop/personal-website
git status
```

- 如果看到 `On branch main`，说明已是 Git 仓库。
- 如果不是 Git 仓库：
```bash
git init
printf ".DS_Store\n" >> .gitignore
git add .
git commit -m "Initial commit"
git branch -M main
```

### 1.2 在 GitHub 创建仓库
在 GitHub 新建仓库（例如 `personal-website`），不要勾选自动创建 README。

### 1.3 绑定远程并首次推送
```bash
cd /Users/lumine/Desktop/personal-website

# 清理可能错误的 origin（可重复执行）
git remote remove origin 2>/dev/null || true

# 绑定你的仓库地址（替换成你自己的）
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO>.git

# 验证
git remote -v

# 首次推送
git push -u origin main
```

---

## 2) Vercel 首次部署（只做一次）

1. 登录 [Vercel](https://vercel.com)
2. `Add New` → `Project`
3. 选择你刚推送的 GitHub 仓库并 `Import`
4. 设置：
   - Framework Preset: `Other`
   - Root Directory: 仓库根目录（默认）
   - Build Command: 留空
   - Output Directory: 留空
5. 点击 `Deploy`

部署完成后会得到一个 `*.vercel.app` 域名。

---

## 3) 每次更新的固定流程（最常用）

```bash
cd /Users/lumine/Desktop/personal-website

# 1) 看改动
git status

# 2) 暂存改动
git add .

# 3) 提交（写清楚本次改动）
git commit -m "Update writings layout and article content"

# 4) 推送
git push
```

推送后，Vercel 会自动触发新部署（通常 1-2 分钟）。

---

## 4) 常见问题排查

### 4.1 `fatal: 'origin' does not appear to be a git repository`
说明远程地址没配对或仓库不存在。

```bash
git remote -v
git remote remove origin
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO>.git
git push -u origin main
```

### 4.2 `nothing to commit, working tree clean`
说明当前没有新改动，不需要 commit，直接检查是否推送过：
```bash
git push
```

### 4.3 权限报错（HTTPS 推送）
- 确认 GitHub 仓库已创建
- 确认你对仓库有写权限
- 使用 GitHub Personal Access Token（PAT）作为认证

---

## 5) Vercel 要不要付费？

结论（截至 2026-03-19）：
- **可以免费用**（Hobby 计划）
- 但 Hobby 仅适用于**个人、非商业用途**
- 超过免费额度后通常不会自动扣费，但功能会受限/暂停，需等待额度窗口恢复或升级 Pro

官方文档：
- Hobby 计划说明（免费）：https://vercel.com/docs/plans/hobby
- 计划总览：https://vercel.com/docs/accounts/plans
- Fair Use（Hobby 仅非商业）：https://vercel.com/docs/limits/fair-use-guidelines

如果你的站点用于商业用途（例如有商业合作、公司项目、营利活动），建议直接用 Pro。
